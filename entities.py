import random
import pygame
import copy
import uuid
from uuid import UUID
import json
import requests
from io import BytesIO
from typings import pokemon_advantages, pokemon_disadvantages, pokemon_null
from data import get_move_data, get_pokemon_stats, get_pokemon_moves
#libraries for path and async loading
import os
import sys
import threading


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 40  # Size of each tile (square)
GRID_WIDTH = SCREEN_WIDTH // TILE_SIZE  # Number of columns
GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE  # Number of rows
BATTLE_PROBABILITY = 0.1  # 10% chance of encountering a wild Pokémon
GRAY = (128, 128, 128)

def create_path(relative_path: str) -> str:
    '''creates and returns the path to the resource depending on if it is
    pyinstaller exe or being run in dev environment'''
    path: str
    if hasattr(sys, '_MEIPASS'):
        path = os.path.join(sys._MEIPASS, relative_path)
    else:
        path = os.path.join(os.path.abspath("."), relative_path)
    return path


def use(move, player_pokemon, opponent):
    """Calculate damage based on move power and level"""
    missed = False
    if player_pokemon.stats['accuracy'] < 100 and (random.random() + player_pokemon.stats['accuracy']/100) < opponent.stats['evasion']/100 and move['category'] != "status":
        missed = True
        return 0, False, False, opponent.name, missed
    damage = move['power']  # Simple damage formula
    ailment_applied = False
    stat_change_applied = False
    target = None
    if move['ailment'] != "none" and opponent.status == "none" and random.random() <= (move['effect_chance'] if move['effect_chance'] != 0 else 100)/100:
        opponent.status = move['ailment']
        ailment_applied = True
    if len(move['stat_changes']) > 0:
        stat_change_applied = True
        for stat_change in move['stat_changes']:
            if stat_change['change'] > 0:
                target = player_pokemon.name
                player_pokemon.stats[stat_change['stat']['name']] += stat_change['change'] * (player_pokemon.stats[stat_change['stat']['name']] * 0.3)
            else:
                target = opponent.name
                opponent.stats[stat_change['stat']['name']] += stat_change['change'] * (opponent.stats[stat_change['stat']['name']] * 0.3)

    return damage, ailment_applied, stat_change_applied, target, missed

#code to make image loading async
# Dictionary to cache loaded images
image_cache = {}

# Placeholder image
placeholder_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
placeholder_image.fill(GRAY)

def load_image_async(image_url, cache_key, callback):
    response = requests.get(image_url)
    image = pygame.image.load(BytesIO(response.content))
    image_cache[cache_key] = image
    callback(image)

def get_image(image_url, callback):
    if image_url in image_cache:
        return image_cache[image_url]
    else:
        # Start a new thread to load the image
        threading.Thread(target=load_image_async, args=(image_url, image_url, callback)).start()
        return placeholder_image



player_pokemon_moves = {}

class Pokemon:
    def __init__(self, name, type, level, moves = [], evolution = None, evolution_level = None, exp = 0, status="none", is_wild=False, caught=False, id = None, stats = None, current_health=None):
        self.name = name
        self.type = type
        self.level = level
        self.moves = [get_move_data(move['name']) if move != 0 else get_move_data("pound") for move in moves ] if isinstance(moves, dict) else [get_move_data(move) if move != 0 else get_move_data("pound") for move in moves ]  # A list of moves that the Pokémon can use
        self.evolution = evolution
        self.evolution_level = evolution_level
        self.evolved = False
        self.learnable_moves = get_pokemon_moves(name.lower())
        self.learnable_moves = [get_move_data(move) for move in self.learnable_moves]
        self.exp = exp  # Experience points
        self.max_exp = 5 * level  # Maximum experience points needed to level up
        self.status = status
        self.is_wild = is_wild  # Identifier to differentiate between wild and player's Pokémon
        self.caught = caught  # Identifier to differentiate between caught or not
        self.id = id if id is not None else uuid.uuid4()
        self.base_stats = get_pokemon_stats(name.lower())  # A dictionary of base stats
        self.stats = stats if stats is not None else self.base_stats.copy() # A dictionary of base stats
        self.current_health = current_health if current_health is not None else self.stats['hp']  # Current health of the PokémonS
        image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{self.stats['id']}.png"
        self.image = get_image(image_url, self.update_image)

    def update_image(self, image):
        self.image = image

    def learn_move(self, move, screen):
        known_moves = [m['name'] for m in self.moves]

        if move['name'] in known_moves:
            while True:
                self.learnable_moves.pop(0)
                move = self.learnable_moves[0]
                if move['name'] not in known_moves:
                    break           
            
        if len(self.moves) < 4:
            self.moves.append(move)
            return f"{self.name} learned {self.learnable_moves[0]['name']}!"
        else:
            return f"{self.name} already knows 4 moves! Should a move be forgotten for {self.learnable_moves[0]['name']}?"
            

    def update_stats(self):
        """Update stats based on the level"""
        healthDiff = self.stats['hp'] - self.current_health
        self.stats['hp'] = self.base_stats['hp'] + (self.level * 3)
        self.stats["attack"] = self.base_stats["attack"] + (self.level * 3)
        self.stats["special-attack"] = self.base_stats["special-attack"] + (self.level * 3)
        self.stats["defense"] = self.base_stats["defense"] + (self.level * 3)
        self.stats["special-defense"] = self.base_stats["special-defense"] + (self.level * 3)
        self.stats["speed"] = self.base_stats["speed"] + (self.level * 3)
        self.stats["accuracy"] = 100
        self.stats["evasion"] = 100
        self.current_health = self.stats['hp'] - healthDiff  # Ensure current health does not exceed max health

    def level_up(self):
        """Level up the Pokémon and update stats"""
        self.level += 1
        self.exp -= self.max_exp
        self.max_exp += self.level * 2
        self.update_stats()

    def take_damage(self, damage):
        """Apply damage to the Pokémon's health"""
        self.current_health = max(0, self.current_health - damage)

    def heal(self, amount):
        """Heal the Pokémon"""
        self.current_health = min(self.stats['hp'], self.current_health + amount)
    
    def heal_status(self):
        self.status = None

    def restore_pp(self, pokemon):
        for i, move in enumerate(pokemon.moves):
            move['pp'] = move['max_pp']

    def is_alive(self):
        """Check if the Pokémon is alive"""
        return self.current_health > 0

    def use_move(self, move, opponent):
        """Use a move on the opponent"""
        if move['pp'] < 1:
            return f"No pp left for this move", False, False, False, False, False, False, False, False
        move['pp'] -= 1
        if move['category'] == "physical":
            damage, ailment_applied, stat_change_applied, target, missed = use(move, self, opponent) 
            damage *= (self.stats["attack"] / opponent.stats["defense"])
            if self.status == "burn":
                damage /= 2
        elif move['category'] == "special":
            damage, ailment_applied, stat_change_applied, target, missed = use(move, self, opponent) 
            damage *= (self.stats["special-attack"] / opponent.stats["special-defense"])
        else:
            damage, ailment_applied, stat_change_applied, target, missed = use(move, self, opponent)
            if missed:
                return damage, False, False, False, False, ailment_applied, stat_change_applied, target, False, missed
            return damage, False, False, False, False, ailment_applied, stat_change_applied, target, False, missed
        
        if missed:
            return damage, False, False, False, False, ailment_applied, stat_change_applied, target, False, missed
        
        damage = ((damage * ((2 * self.level / 5) + 2))/30 + 2)   # Apply the damage formula
        if self.type == move['type']:
            damage *= 1.5  # Apply STAB (Same Type Attack Bonus)
        is_critical = random.random() < move['crit_chance'] + 0.1  # 10% chance of a critical hit
        is_effective = is_not_effective = is_null = False
        num_hits_text = None
        if is_critical:
            damage *= 1.5  # Apply critical hit multiplier
        if opponent.type in pokemon_advantages[move['type']]:
            damage *= 2  # Apply type advantage
            is_effective = True
        elif opponent.type in pokemon_disadvantages[move['type']]:
            damage /= 2
            is_not_effective = True
        elif opponent.type in pokemon_null[move['type']]:
            damage = 0
            is_null = True
        num_hits = random.randint(move['min_hits'], move['max_hits'])
        damage *= num_hits
        if move['max_hits'] > 1:
            num_hits_text = f"Hit {num_hits} time(s)!"
        damage = round(damage)  # Round to the nearest integer
        opponent.take_damage(damage)  # Apply the damage to the opponent
        return damage, is_critical, is_effective, is_not_effective, is_null, ailment_applied, stat_change_applied, target, num_hits_text, missed

    def draw(self, screen, x, y):
        """Draw the Pokémon's name and health bar"""
        font = pygame.font.SysFont(None, 30)
        name_text = font.render(f"{self.name} (Lv {self.level})", True, (0, 0, 0))
        health_text = font.render(f"HP: {self.current_health}/{self.stats['hp']}", True, (0, 0, 0))
        screen.blit(name_text, (x, y))
        screen.blit(health_text, (x, y + 30))



#load player data function
def load_player_data(playerS):
    def convert_str_to_uuid(data):
        if isinstance(data, dict):
            # Remove useless key if it exists
            data.pop('base_stats', None)
            data.pop('learnable_moves', None)
            data.pop('max_exp', None)
            data.pop('evolved', None)
            data.pop('image', None)
            return {key: convert_str_to_uuid(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [convert_str_to_uuid(item) for item in data]
        elif isinstance(data, str):
            try:
                return UUID(data)
            except ValueError:
                return data
        else:
            return data

    try:
        with open("player_data.json", "r") as file:
            data = json.load(file)
            player.pokemon_team = [Pokemon(**convert_str_to_uuid(pokemon)) for pokemon in data["pokemon_team"]]
            player.inventory = convert_str_to_uuid(data["inventory"])
            player.pc = [Pokemon(**convert_str_to_uuid(pokemon)) for pokemon in data["pc"]]

            return True, data["regions"], data["region_pokedex"]

    except FileNotFoundError:
        return False, None, None

class Player:
    def __init__(self, grid_x, grid_y, inventory={"pokeball":2, "super potion":2, "status heal":2, "pp restore":2}):
        self.pokemon_team = []  # List of Pokémon in the player's team
        self.pc = []  # List of Pokémon in the player's PC
        self.grid_x = grid_x  # Player's column in the grid
        self.grid_y = grid_y  # Player's row in the grid
        self.inventory = inventory  # Dictionary to store items
        self.item_in_use = False  # Flag to check if an item is being used
        self.width = 40
        self.height = 40
        self.speed = 0.1  # Speed at which the player moves

        # Load the player image
        self.image = [pygame.image.load(create_path('Assets\Player\player_walking_down1.png'))]
        self.frame = 0  # Frame counter for animation

    def update_frame(self):
        """Update the frame counter for animation"""
        self.frame = (self.frame + 1) % len(self.image)
    
    def move(self, dx, dy, GRID_WIDTH, GRID_HEIGHT):
        """Move the player by dx, dy in terms of grid tiles"""
        # Calculate the new grid position
        new_x = self.grid_x + dx
        new_y = self.grid_y + dy

        # Prevent the player from moving off the grid
        if 0 <= new_x < GRID_WIDTH:
            self.grid_x = new_x  # Update x if within bounds
        if 0 <= new_y < GRID_HEIGHT:
            self.grid_y = new_y  # Update y if within bounds

    def draw(self, screen, TILE_SIZE):
        """Draw the player on the screen"""
        # Define a scaling factor
        scaling_factor = 4.5  # For example, make the image 1.5 times larger

        # Select the current frame
        current_image = self.image[self.frame]

        # Scale the image to the desired size
        scaled_width = int(TILE_SIZE * scaling_factor)
        scaled_height = int(TILE_SIZE * scaling_factor)
        scaled_image = pygame.transform.scale(current_image, (scaled_width, scaled_height))

        # Calculate the position to center the larger image on the tile
        draw_x = self.grid_x * TILE_SIZE - (scaled_width - TILE_SIZE) // 2
        draw_y = self.grid_y * TILE_SIZE - (scaled_height - TILE_SIZE) // 2

        # Draw the scaled image on the screen
        screen.blit(scaled_image, (draw_x, draw_y - TILE_SIZE//2))

    def choose_pokemon(self, choice=0):
        # Simplified; normally you'd want more advanced selection logic
        if choice >= len(self.pokemon_team):
            return "None"
        return self.pokemon_team[choice]

    def attempt_catch(self, wild_pokemon):
        # Chance to catch depends on Pokémon health and type of Pokéball
        catch_chance = 1 - wild_pokemon.current_health/wild_pokemon.stats['hp']
        if wild_pokemon.status != None:
            catch_chance += 0.1
        if random.random() < catch_chance:
            new_pokemon = Pokemon(wild_pokemon.name, wild_pokemon.type, wild_pokemon.level, wild_pokemon.moves, wild_pokemon.evolution, wild_pokemon.evolution_level)
            new_pokemon.update_stats()
            new_pokemon.is_wild = False
            if len(self.pokemon_team) < 6:
                self.pokemon_team.append(new_pokemon)
            else:
                self.pc.append(new_pokemon)
            return True
        else:
            return False
        
    def use_item(self, item, pokemon):
        """Use an item on the Pokémon"""
        
        if self.inventory[item] < 1:
            return f"No {item}s left!"
        if item == "pokeball":
            return f"Can't use a Pokéball outside of battle!"
        elif item == "super potion":
            if pokemon.current_health < pokemon.stats['hp']:
                self.inventory[item] -= 1
                text = f"{pokemon.name} was healed by {min(50, pokemon.stats['hp'] - pokemon.current_health)} HP!"
                pokemon.heal(50)
                return text
            return f"{pokemon.name} is already at full health!"
        elif item == "status heal":
            self.inventory[item] -= 1
            pokemon.heal_status()
            return f"{pokemon.name} was healed of all status conditions!"
        elif item == "pp restore":
            self.inventory[item] -= 1
            if pokemon.id not in player_pokemon_moves:
                player_pokemon_moves[pokemon.id] = copy.deepcopy(pokemon.moves)
            pokemon.restore_pp(pokemon)
            return f"{pokemon.name}'s PP was restored!"
        else:
            return f"Invalid item!"

player = Player(GRID_WIDTH // 2, GRID_HEIGHT // 2)  # Create a player object at the center of the grid
