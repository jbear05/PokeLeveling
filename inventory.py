import pygame
import copy
import math
from entities import Pokemon, Player, player, player_pokemon_moves, create_path
from battle import Button, Item

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
DARK_RED = (139, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
LIGHT_GREEN = (144, 238, 144)
GOLD = (255, 215, 0)
ORANGE = (255, 165, 0)
LIGHT_ORANGE = (255, 200, 111)
PURPLE = (128, 0, 128)
LIGHT_PURPLE = (221, 160, 221)
PINK = (255, 192, 203)
LIGHT_PINK = (255, 182, 193)
YELLOW = (255, 255, 0)
BROWN = (165, 42, 42)
DARK_BROWN = (139, 69, 19)
DARK_GRAY = (169, 169, 169)
GRAY = (128, 128, 128)
LIGHT_GRAY = (211, 211, 211)

pokemon_images = []
pc_pokemon_images = []

def display_buttons(screen, player, buttons):
    # Display items as buttons
    for button in buttons:
        button.draw(screen)
    
    # Handle button hover
    mouse_pos = pygame.mouse.get_pos()
    for button in buttons:
        button.check_hover(mouse_pos)

def display_pokemon_buttons(screen, player, buttons):
    # Display Pokémon as buttons
    
    for i in range(len(buttons)):
        buttons[i].draw(screen)
        screen.blit(pokemon_images[i][0], pokemon_images[i][1])
    
    # Handle button hover
    mouse_pos = pygame.mouse.get_pos()
    for button in buttons:
        button.check_hover(mouse_pos)

def get_item(item):
    return item

def get_pokemon(pokemon_id, moves):
    return pokemon_id, moves

def create_pokemon_buttons(screen):
    font = pygame.font.Font(None, 24)
    # create Pokémon buttons
    pokemon_buttons = []
    global pokemon_images
    pokemon_images = []
    for i, pokemon in enumerate(player.pokemon_team):
        pokemon.update_stats()
        if pokemon.id not in player_pokemon_moves:
            player_pokemon_moves[pokemon.id] = copy.deepcopy(pokemon.moves)
        pokemon_buttons.append(Button(450, 130 + 70 * i, 260, 50, f"{pokemon.name} - LV: {pokemon.level} - HP: {pokemon.current_health}/{pokemon.stats['hp']}",  font, (50, 130, 217), WHITE, lambda pokemon=pokemon: get_pokemon(pokemon.id, player_pokemon_moves[pokemon.id]), BLACK))

        # Load Pokémon images
        pokemon_image = pygame.image.load(create_path(f'Assets\Pokemon\{pokemon.name}.png'))
        # Scale the Pokémon images
        pokemon_image = pygame.transform.scale(pokemon_image, (80, 80))  # Scale to 100x100 pixels
        pokemon_image_rect = pokemon_image.get_rect(midtop=(750, pokemon_buttons[i].y - 15))
        pokemon_images.append((pokemon_image, pokemon_image_rect))
    
    return pokemon_buttons
    

def create_item_buttons(player, screen, SCREEN_WIDTH):
    font = pygame.font.Font(None, 25)
    item_buttons = []
    item_count = 0
    for item, quantity in player.inventory.items():
        item_buttons.append(Button(150, 200 + 70 * item_count, 200, 50, f"{item}s: {quantity}",  font, LIGHT_ORANGE, BLACK, lambda item=item: get_item(item), BLACK))
        item_count += 1
    return item_buttons


def move_pokemon_to_pc(player, pokemon):
    if len(player.pokemon_team) <= 1:
        return "You can't have less than 1 Pokémon in your team!"
    else:
        player.pokemon_team.remove(pokemon)
        player.pc.append(pokemon)
        return "Pokémon moved to PC!"

def move_pokemon_to_team(player, pokemon):
    if len(player.pokemon_team) >= 6:
        return "You can't have more than 6 Pokémon in your team!"
    elif pokemon.current_health <= 0:
        return "You can't add a fainted Pokémon to your team!"
    else:
        player.pc.remove(pokemon)
        player.pokemon_team.append(pokemon)
        return "Pokémon added to team!"

def create_pc_pokemon_buttons(screen, player, SCREEN_WIDTH, page):
    font = pygame.font.Font(None, 20)
    pc_pokemon_buttons = []
    global pc_pokemon_images
    pc_pokemon_images = []
    for i, pokemon in enumerate(player.pc[page * 21:(page + 1) * 21]):
        pokemon.update_stats()
        pc_pokemon_buttons.append(Button(SCREEN_WIDTH // 12 + 260 * math.floor((i) / 7), 50 + 70 * (i - (7 * math.floor(i/7))), 200, 50, f"{pokemon.name} - LV:{pokemon.level} - HP:{pokemon.current_health}/{pokemon.stats['hp']}", font, (DARK_GREEN if pokemon.current_health > 0 else DARK_RED), WHITE, lambda pokemon=pokemon: move_pokemon_to_team(player, pokemon), BLACK))
        # Load Pokémon images
        pc_pokemon_image = pygame.image.load(create_path(f'Assets\Pokemon\{pokemon.name}.png'))
        # Scale the Pokémon images
        pc_pokemon_image = pygame.transform.scale(pc_pokemon_image, (64, 64))  # Scale to 100x100 pixels
        pc_pokemon_image_rect = pc_pokemon_image.get_rect(midtop=(pc_pokemon_buttons[i].x - 30, pc_pokemon_buttons[i].y - 5))
        pc_pokemon_images.append((pc_pokemon_image, pc_pokemon_image_rect))
    return pc_pokemon_buttons

def display_pc_pokemon_buttons(screen, player, buttons):
    # Display items as buttons
    for i in range(len(buttons)):
        buttons[i].draw(screen)
        screen.blit(pc_pokemon_images[i][0], pc_pokemon_images[i][1])
    
    # Handle button hover
    mouse_pos = pygame.mouse.get_pos()
    for button in buttons:
        button.check_hover(mouse_pos)




