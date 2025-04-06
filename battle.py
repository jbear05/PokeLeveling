import pygame
import time
import random
import copy
import requests
from io import BytesIO
from entities import Pokemon, Player, player, player_pokemon_moves, create_path
from typings import pokemon_disadvantages, pokemon_null, pokemon_advantages
from pokedex import pokedex


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
DARK_RED = (139, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (144, 238, 144)
GOLD = (255, 215, 0)
ORANGE = (255, 165, 0)
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

class Button:
    def __init__(self, x, y, width, height, text, font, bg_color, text_color, action, border_color, move_info = None, border_width = 2):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color
        self.hovered = False
        self.action = action
        self.border_color = border_color
        self.border_width = border_width
        self.move_info = move_info

    def draw(self, screen):
        color = self.border_color if self.hovered and self.border_color != BLACK else self.bg_color
        border_color = self.bg_color if self.hovered else self.border_color
        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        pygame.draw.rect(screen, border_color, self.rect, self.border_width, border_radius=5)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        # Display move information if hovered
        if self.hovered and self.move_info:
            info_surface = self.font.render(self.move_info, True, BLACK)
            info_rect = info_surface.get_rect(center=(screen.get_width() // 2, 250))
            screen.blit(info_surface, info_rect)

    def check_hover(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if self.text != "None":
                return True
            return False

button_border_types = {
    "normal": GRAY,
    "fire": RED,
    "water": BLUE,
    "grass": GREEN,
    "electric": YELLOW,
    "ice": LIGHT_BLUE,
    "fighting": ORANGE,
    "poison": PURPLE,
    "ground": BROWN,
    "flying": LIGHT_GRAY,
    "psychic": PINK,
    "bug": LIGHT_GREEN,
    "rock": DARK_BROWN,
    "ghost": LIGHT_PURPLE,
    "dragon": GOLD,
    "dark": BLACK,
    "steel": DARK_GRAY,
    "fairy": LIGHT_PINK
}

class Item:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def use(self, pokemon, player, caught_ok):
        if player.inventory[self.name] > 0:
            player.inventory[self.name] -= 1
            if self.name == "pokeball":
                caught_ok[0] = self.effect(player)
            elif self.name == "pp restore":
                self.effect(pokemon)
            elif self.name == "status heal":
                self.effect(pokemon)
            elif self.name == "super potion":
                self.effect(pokemon)
            return f"Player used {self.name}"
        else:
            return "You don't have any of this item"

#exp bar
def draw_exp_bar(screen, x, y, current_exp, max_exp):
    """Draw the EXP bar"""
    bar_width = 200
    bar_height = 10
    exp_ratio = current_exp / max_exp
    pygame.draw.rect(screen, BLACK, (x, y, bar_width, bar_height))  # Background bar
    pygame.draw.rect(screen, BLUE, (x, y, bar_width * exp_ratio, bar_height))  # Filled bar

def battle(screen, width, height, battle_stage, player_pokemon, opponent_pokemon):
    player_pokemon.update_stats()  # Update stats based on the level
    opponent_pokemon.update_stats()  # Update stats based on the level
    """Simulate a battle with a simple menu and player options"""
    battle_over = False
    font = pygame.font.SysFont(None, 30)

    if player_pokemon.id not in player_pokemon_moves:
        player_pokemon_moves[player_pokemon.id] = player_pokemon.moves

    # Initialize variables
    critical_hit_text = None
    effective_text = None
    ailment_text = None
    stat_change_text = None
    num_hits_text = None
    caught_ok = [False]

    # Define battle states
    PLAYER_TURN = 0
    PLAYER_MOVE = 1
    OPPONENT_TURN = 2
    OPPONENT_MOVE = 3
    STATUS_CHECK = 4
    state = PLAYER_TURN if player_pokemon.stats["speed"] >= opponent_pokemon.stats["speed"] else OPPONENT_TURN

    #Determine battle stage based on environment
    if battle_stage == 1:
        stage = pygame.image.load(create_path(f'Assets\Battle\grass_battle_stage.png'))
    elif battle_stage == 2:
        stage = pygame.image.load(create_path(f'Assets\Battle\water_battle_stage.png'))
    elif battle_stage == 3:
        stage = pygame.image.load(create_path(f'Assets\Battle\\fire_battle_stage.png'))
    elif battle_stage == 4:
        stage = pygame.image.load(create_path(f'Assets\Battle\sand_battle_stage.png'))
    elif battle_stage == 5:
        stage = pygame.image.load(create_path(f'Assets\Battle\snow_battle_stage.png'))
    elif battle_stage == 6:
        stage = pygame.image.load(create_path(f'Assets\Battle\\factory_battle_stage.png'))
    elif battle_stage == 7:
        stage = pygame.image.load(create_path(f'Assets\Battle\graveyard_battle_stage.png'))
    elif battle_stage == 8:
        stage = pygame.image.load(create_path(f'Assets\Battle\\forest_battle_stage.png'))
    elif battle_stage == 9:
        stage = pygame.image.load(create_path(f'Assets\Battle\dojo_battle_stage.png'))
    elif battle_stage == 10:
        stage = pygame.image.load(create_path(f'Assets\Battle\clouds_battle_stage.png'))
    elif battle_stage == 11:
        stage = pygame.image.load(create_path(f'Assets\Battle\swamp_battle_stage.png'))
    elif battle_stage == 12:
        stage = pygame.image.load(create_path(f'Assets\Battle\dragons_den_battle_stage.png'))
    #Scale the stage
    stage = pygame.transform.scale(stage, (width, height))

    caught_image = pygame.image.load(create_path('Assets\Battle\caught_sign.png'))

    # Scale the Pokémon images
    player_pokemon_image = pygame.transform.scale(player_pokemon.image, (100, 100))  # Scale to 100x100 pixels
    opponent_pokemon_image = pygame.transform.scale(opponent_pokemon.image, (100, 100))  # Scale to 100x100 pixels

     # Define the positions for the health bars
    player_health_bar_rect = pygame.Rect(50, 100, 200, 20)
    opponent_health_bar_rect = pygame.Rect(550, 100, 200, 20)

    # Define the positions for the Pokémon images
    player_pokemon_image_rect = player_pokemon_image.get_rect(midtop=(player_health_bar_rect.centerx, player_health_bar_rect.bottom + 20))
    opponent_pokemon_image_rect = opponent_pokemon_image.get_rect(midtop=(opponent_health_bar_rect.centerx, opponent_health_bar_rect.bottom + 20))

    items = {
    "super potion" : Item("super potion", "Heals 50 HP", lambda pokemon: pokemon.heal(50)),
    "pokeball" : Item("pokeball", "Catches a wild Pokemon", lambda player: player.attempt_catch(opponent_pokemon)),
    "pp restore" : Item("pp restore", "Restores 10 PP", lambda pokemon: pokemon.restore_pp(player_pokemon)),
    "status heal" : Item("status heal", "Heals status conditions", lambda pokemon: pokemon.heal_status()),
    }

    # Create buttons for each move
    move_buttons = []
    for i, move in enumerate(player_pokemon.moves):
        move_buttons.append(Button(
            50, 310 + 70 * i, 200, 50,
            f"{move['name']}: {move['pp']}",
            font, WHITE, BLACK,
            lambda move=move: player_pokemon.use_move(player_pokemon_moves[player_pokemon.id].get(move), opponent_pokemon),
            button_border_types[move['type']], f"Power: {move['power']} Category: {move['category']}"
        ))

    item_buttons = []
    item_count = 0
    for item in player.inventory:
        item_buttons.append(Button(50, 310 + 70 * item_count, 200, 50, f"{items[item].name}s: {player.inventory[item]}",  font, GRAY, BLACK, lambda item=item: items[item].use(player_pokemon, player, caught_ok), BLACK))
        item_count += 1

    pokemon_buttons = []
    for i in range(3):
        if i < len(player.pokemon_team):
            pokemon_buttons.append(Button(50, 310 + 70 * i, 200, 50, f"{player.pokemon_team[i].name}: {player.pokemon_team[i].current_health}/{player.pokemon_team[i].stats['hp']}",  font, WHITE, BLACK, lambda i=i: player.choose_pokemon(i), button_border_types[player.pokemon_team[i].type]))
        else:
            pokemon_buttons.append(Button(50, 310 + 70 * i, 200, 50, "None",  font, GRAY, BLACK, lambda: None, BLACK))
    for i in range(3, 6):
        if i < len(player.pokemon_team):
            pokemon_buttons.append(Button(270, 310 + 70 * (i - 3), 200, 50, f"{player.pokemon_team[i].name}: {player.pokemon_team[i].current_health}/{player.pokemon_team[i].stats['hp']}",  font, WHITE, BLACK, lambda i=i: player.choose_pokemon(i), button_border_types[player.pokemon_team[i].type]))
        else:
            pokemon_buttons.append(Button(270, 310 + 70 * (i - 3), 200, 50, "None",  font, GRAY, BLACK, lambda: None, BLACK))


    # Initialize menu states
    showing_moves = False
    showing_items = False
    showing_pokemon = False

    def show_menu(buttons):
        """Show the move buttons"""
        for button in buttons:
            button.draw(screen)

        # Handle button hover
        mouse_pos = pygame.mouse.get_pos()
        for button in buttons:
            button.check_hover(mouse_pos)
    
    def try_to_run():
        escape_chance = 0.5 * (player_pokemon.level / opponent_pokemon.level) # 50% chance to escape
        if random.random() < escape_chance:
            return True
        return False

    # create menu buttons
    menu_buttons = []
    menu_buttons.append(Button(550, 310 + 70 * 0, 200, 50, "Run", font, BLUE, BLACK, lambda: try_to_run(), LIGHT_BLUE))
    menu_buttons.append(Button(550, 310 + 70 * 1, 200, 50, "Bag", font, GOLD, BLACK, lambda: False, YELLOW))
    menu_buttons.append(Button(550, 310 + 70 * 2, 200, 50, "Pokemon", font, GREEN, BLACK, lambda: False, LIGHT_GREEN))
    menu_buttons.append(Button(550, 310 + 70 * 3, 200, 50, "Fight", font, DARK_RED, BLACK, lambda: False, RED))

    battle_text = f"{player_pokemon.name}'s turn!" if state == PLAYER_TURN else f"{opponent_pokemon.name}'s turn!"
    
    new_move_text = None
    evolution_text = None
    replacing_move = False
    dont_learn_move_button = Button(270, 310, 200, 50, "No",  font, GRAY, BLACK, lambda: False, BLACK)
    exp_added = False

    #speed check flags
    opponent_moved = False
    player_moved = False

    # Create a font for displaying stats
    stats_font = pygame.font.Font(None, 20)

    def draw_pokemon_stats(pokemon, x, y):
        stats_text = f"ATK:{round(pokemon.stats['attack'])} SPATK:{round(pokemon.stats['special-attack'])} DEF:{round(pokemon.stats['defense'])} SPDEF:{round(pokemon.stats['special-defense'])} SPD:{round(pokemon.stats['speed'])}"
        stats_surface = stats_font.render(stats_text, True, BLACK)
        screen.blit(stats_surface, (x, y))

    poisonCheck = True
    burnCheck = True

    while not battle_over:
        screen.fill(WHITE)
        # Draw the background
        screen.blit(stage, (0, 0))

        # Draw the player's and opponent's Pokémon
        player_pokemon.draw(screen, 50, 50)
        opponent_pokemon.draw(screen, 550, 50)

        # Draw Pokémon stats
        draw_pokemon_stats(player_pokemon, 15, 30)
        draw_pokemon_stats(opponent_pokemon, 515, 30)

        # Draw a health bar for the opponent (red for opponent, green for player)
        pygame.draw.rect(screen, RED, opponent_health_bar_rect)  # Opponent health bar
        pygame.draw.rect(screen, GREEN, (550, 100, (200 * opponent_pokemon.current_health) / opponent_pokemon.stats['hp'], 20))
        #check if opponent pokemon has already been caught
        for pokemon in player.pokemon_team:
            if opponent_pokemon.name == pokemon.name:
                opponent_pokemon.caught = True
        for pokemon in player.pc:
            if opponent_pokemon.name == pokemon.name:
                opponent_pokemon.caught = True
        # Draw a sign to show if pokemon is caught next to their name
        if pokedex[opponent_pokemon.name].caught:
            # Load the caught image
            # Replace the text rendering with the image rendering
            caught_sign_rect = caught_image.get_rect(center=(opponent_health_bar_rect.right + 20, opponent_health_bar_rect.centery))
            screen.blit(caught_image, caught_sign_rect)
        pygame.draw.rect(screen, RED, player_health_bar_rect)  # Player health bar
        pygame.draw.rect(screen, GREEN, (50, 100, (200 * player_pokemon.current_health) / player_pokemon.stats['hp'], 20))
        
        # Draw the EXP bar for the player
        draw_exp_bar(screen, 50, 130, min(player_pokemon.exp, player_pokemon.max_exp), player_pokemon.max_exp)

        # Blit the Pokémon images below the health bars
        screen.blit(player_pokemon_image, player_pokemon_image_rect)
        screen.blit(opponent_pokemon_image, opponent_pokemon_image_rect)


        # Draw the menu buttons
        for button in menu_buttons:
            button.draw(screen)
        
        # Handle button hover
        mouse_pos = pygame.mouse.get_pos()
        for button in menu_buttons:
            button.check_hover(mouse_pos)

        # Draw the move buttons if showing_moves is True
        if showing_moves:
            show_menu(move_buttons)

        # Draw the item buttons if showing_items is True
        if showing_items:
            show_menu(item_buttons)

        if showing_pokemon:
            show_menu(pokemon_buttons)
        
        if replacing_move:
            show_menu([dont_learn_move_button])
        
        # Display battle text
        battle_text_surface = font.render(battle_text, True, (0, 0, 0))
        battle_text_rect = battle_text_surface.get_rect(center=(screen.get_width() // 2, 200))
        screen.blit(battle_text_surface, battle_text_rect)

        # Update the screen
        pygame.display.flip()
        if battle_text == f"You ran away!":
            pygame.time.delay(1000)  # Add a small delay to slow down the battle
            battle_over = True
            return False
        elif battle_text == f"You lost the battle!":
            pygame.time.delay(1000)  # Add a small delay to slow down the battle
            battle_text = "Game Over!"
            continue
        elif battle_text == "Game Over!":
            pygame.time.delay(2000)  # Wait for 2 seconds before quitting
            battle_over = True
        elif battle_text == f"You won the battle!" or battle_text == f"You won the battle! {player_pokemon.name} leveled up to level {player_pokemon.level}!":
            pygame.time.delay(1000)  # Add a small delay to slow down the battle
            if new_move_text:
                battle_text = new_move_text
                continue
            elif evolution_text:
                battle_text = evolution_text
                continue
            else:
                battle_over = True
                continue
        elif battle_text == new_move_text:
            if new_move_text == f"{player_pokemon.name} already knows 4 moves! Should a move be forgotten for {player_pokemon.learnable_moves[0]['name']}?":
                showing_moves = True
                showing_items = False
                showing_pokemon = False
                replacing_move = True
                new_move_text = None
                state = PLAYER_TURN
                continue
            else:
                new_move_text = None
                continue
        elif battle_text == evolution_text:
            evolution_text = None
            continue
        elif battle_text == f"{player_pokemon.name} learned {player_pokemon.learnable_moves[0]['name']}!":
            pygame.time.delay(1000)
            player_pokemon.learnable_moves.pop(0)
            if player_pokemon.exp < player_pokemon.max_exp:
                battle_over = True
                continue
        elif battle_text == f"{player_pokemon.name} didn't learn {player_pokemon.learnable_moves[0]['name']}":
            player_pokemon.learnable_moves.pop(0)
            pygame.time.delay(1000)  # Add a small delay to slow down the battle
            if player_pokemon.exp < player_pokemon.max_exp:
                battle_over = True
                continue
        elif battle_text == f"Player used pokeball":
            pygame.time.delay(1000)
            battle_text = f"..."
            continue
        elif battle_text == f"{player_pokemon.name} fainted!":
            pygame.time.delay(1000)
            player_pokemon = player.choose_pokemon(0)
            player_pokemon_image = pygame.transform.scale(player_pokemon.image, (100, 100))  # Scale to 100x100 pixels
            battle_text = f"{player_pokemon.name} is ready to fight!"
            continue
        elif battle_text == f"{player_pokemon.name} is ready to fight!":
            pygame.time.delay(1000)
            battle_text = f"{player_pokemon.name}'s turn!"
            state = PLAYER_TURN
            continue
        elif battle_text != f"{player_pokemon.name}'s turn!" and battle_text != f"You don't have any of this item" and battle_text != f"{player_pokemon.name} woke up!" and battle_text != f"No pp left for this move" and battle_text != f"{player_pokemon.name} already knows 4 moves! Should a move be forgotten for {player_pokemon.learnable_moves[0]['name']}?" and battle_text != f"{player_pokemon.name} is trapped you can't run away!" and battle_text != f"{player_pokemon.name} is no longer confused!" and battle_text != f"{player_pokemon.name} thawed out!":
            pygame.time.delay(750)

        if caught_ok[0] and battle_text == f"...":
            battle_text = f"You caught the Pokemon!"
            player_pokemon_moves[player.pokemon_team[-1].id] = player.pokemon_team[-1].moves
            opponent_pokemon.current_health = 0
            showing_items = False
            continue
        elif battle_text == f"..." and not caught_ok[0]:
            battle_text = f"You couldn't catch the Pokemon!"
            continue
        
        # Check if the battle is over
        if not player_pokemon.is_alive() and not critical_hit_text and not effective_text and not ailment_text and not stat_change_text and not num_hits_text and not battle_over:
            if player_pokemon in player.pokemon_team:
                player.pc.append(player_pokemon)
                player.pokemon_team.remove(player_pokemon)
            if len(player.pokemon_team) == 0:
                battle_text = f"You lost the battle!"
                result = False
            else:
                battle_text = f"{player_pokemon.name} fainted!"

        elif not opponent_pokemon.is_alive() and not critical_hit_text and not effective_text and not ailment_text and not stat_change_text and not num_hits_text and not battle_over and not replacing_move:
            battle_text = f"You won the battle!"
            result = True
            if not exp_added:
                player_pokemon.exp += 20 * max((opponent_pokemon.level - player_pokemon.level + 1), 1.5) * max(player_pokemon.level / 10, 1)
            if player_pokemon.exp >= player_pokemon.max_exp:
                while player_pokemon.exp >= player_pokemon.max_exp:
                    player_pokemon.level_up()
                    battle_text += f" {player_pokemon.name} leveled up to level {player_pokemon.level}!"
                    if player_pokemon.evolution is not None and player_pokemon.level >= player_pokemon.evolution_level:
                        exp_added = True
                        player_pokemon.evolved = True
                        evolution_text = f"{player_pokemon.name} evolved into {player_pokemon.evolution}!"

                    if max(1, (player_pokemon.level - 5)) % 3 == 0:
                        exp_added = True #variable to check if exp has been added
                        new_move_text = player_pokemon.learn_move(player_pokemon.learnable_moves[0], screen)
                        move_buttons = []
                        for i, move in enumerate(player_pokemon.moves):
                            move_buttons.append(Button(
                                50, 310 + 70 * i, 200, 50,
                                f"{move['name']}: {move['pp']}",
                                font, WHITE, BLACK,
                                lambda move=move: player_pokemon.use_move(player_pokemon_moves[player_pokemon.id].get(move), opponent_pokemon),
                                button_border_types[move['type']], f"Power: {move['power']} Category: {move['category']}"
                            ))
                        new_move = player_pokemon.learnable_moves[0]
                        break
            continue
            

        

        # Handle events based on the current state
        # Add a timer event to ensure the game state is updated periodically
        pygame.time.set_timer(pygame.USEREVENT + 1, 100)  # Set a timer for 100 milliseconds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            
            #Handle the timer event to update the game state
            if event.type == pygame.USEREVENT + 1:
                pygame.time.set_timer(pygame.USEREVENT + 1, 0) # Stop the timer

            if state == PLAYER_TURN:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not replacing_move:  # Left mouse button
                    for button in menu_buttons:
                        if button.check_click(mouse_pos):
                            result = button.action()
                            if button.text == "Fight":
                                move_buttons = []
                                for i, move in enumerate(player_pokemon.moves):
                                    move_buttons.append(Button(
                                        50, 310 + 70 * i, 200, 50,
                                        f"{move['name']}: {move['pp']}",
                                        font, WHITE, BLACK,
                                        lambda move=move: player_pokemon.use_move(move, opponent_pokemon),
                                        button_border_types[move['type']], f"Power: {move['power']} Category: {move['category']}"
                                    ))
                                showing_moves = True
                                showing_items = False
                                showing_pokemon = False
                            elif button.text == "Bag":
                                item_buttons = []
                                item_count = 0
                                for item in player.inventory:
                                    item_buttons.append(Button(50, 310 + 70 * item_count, 200, 50, f"{items[item].name}s: {player.inventory[item]}",  font, GRAY, BLACK, lambda item=item: items[item].use(player_pokemon, player, caught_ok), BLACK))
                                    item_count += 1
                                showing_items = True
                                showing_moves = False
                                showing_pokemon = False
                            elif button.text == "Run" and player_pokemon.status == "trap":
                                battle_text = f"{player_pokemon.name} is trapped you can't run away!"
                                state = PLAYER_TURN
                                pygame.time.set_timer(pygame.USEREVENT, 2000)  # Set a timer for 2 seconds
                            elif button.text == "Run" and result:
                                battle_text = f"You ran away!"
                                pygame.time.set_timer(pygame.USEREVENT, 2000)  # Set a timer for 2 seconds
                            elif button.text == "Run" and not result:
                                battle_text = f"You couldn't escape!"
                                state = OPPONENT_TURN
                                pygame.time.set_timer(pygame.USEREVENT, 2000)  # Set a timer for 2 seconds
                            elif button.text == "Pokemon":
                                pokemon_buttons = []
                                for i in range(3):
                                    if i < len(player.pokemon_team):
                                        pokemon_buttons.append(Button(50, 310 + 70 * i, 200, 50, f"{player.pokemon_team[i].name}: {player.pokemon_team[i].current_health}/{player.pokemon_team[i].stats['hp']}",  font, WHITE, BLACK, lambda i=i: player.choose_pokemon(i), button_border_types[player.pokemon_team[i].type]))
                                    else:
                                        pokemon_buttons.append(Button(50, 310 + 70 * i, 200, 50, "None",  font, GRAY, BLACK, lambda: None, BLACK))
                                for i in range(3, 6):
                                    if i < len(player.pokemon_team):
                                        pokemon_buttons.append(Button(270, 310 + 70 * (i - 3), 200, 50, f"{player.pokemon_team[i].name}: {player.pokemon_team[i].current_health}/{player.pokemon_team[i].stats['hp']}",  font, WHITE, BLACK, lambda i=i: player.choose_pokemon(i), button_border_types[player.pokemon_team[i].type]))
                                    else:
                                        pokemon_buttons.append(Button(270, 310 + 70 * (i - 3), 200, 50, "None",  font, GRAY, BLACK, lambda: None, BLACK))

                                showing_moves = False
                                showing_items = False
                                showing_pokemon = True

                            else:
                                showing_moves = False
                if showing_moves and replacing_move and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, button in enumerate(move_buttons):
                        if button.check_click(mouse_pos):
                            player_pokemon.moves[i] = new_move
                            showing_moves = False
                            battle_text = f"{player_pokemon.name} learned {player_pokemon.learnable_moves[0]['name']}!"
                            replacing_move = False
                            break
                    if dont_learn_move_button.check_click(mouse_pos):
                        battle_text = f"{player_pokemon.name} didn't learn {player_pokemon.learnable_moves[0]['name']}"
                        replacing_move = False
                    break

                elif showing_moves and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not replacing_move:  # Left mouse button
                    for button in move_buttons:
                        if button.check_click(mouse_pos):
                            if player_pokemon.status == "sleep":
                                battle_text = f"{player_pokemon.name} is asleep!"
                                showing_moves = False
                                state = STATUS_CHECK
                                break
                            elif player_pokemon.status == "confusion":
                                battle_text = f"{player_pokemon.name} is confused!"
                                showing_moves = False
                                state = STATUS_CHECK
                                break
                            elif player_pokemon.status == "paralysis" and random.random() < 0.6:
                                battle_text = f"{player_pokemon.name} is paralyzed and can't move!"
                                showing_moves = False
                                state = PLAYER_MOVE
                                break
                            elif player_pokemon.status == "freeze":
                                battle_text = f"{player_pokemon.name} is frozen solid!"
                                showing_moves = False
                                state = STATUS_CHECK
                                break
                            damage, is_critical, is_effective, is_not_effective, is_null, ailment_applied, stat_change_applied, target, num_hits_text, missed = button.action()
                            if damage == f"No pp left for this move":
                                battle_text = damage
                                state = PLAYER_TURN
                            elif missed:
                                battle_text = f"{player_pokemon.name} missed!"
                                state = PLAYER_MOVE
                            else:
                                move_buttons = []
                                for i, move in enumerate(player_pokemon.moves):
                                    move_buttons.append(Button(
                                        50, 310 + 70 * i, 200, 50,
                                        f"{move['name']}: {move['pp']}",
                                        font, WHITE, BLACK,
                                        lambda move=move: player_pokemon.use_move(player_pokemon_moves[player_pokemon.id].get(move), opponent_pokemon),
                                        button_border_types[move['type']], f"Power: {move['power']} Category: {move['category']}"
                                    ))
                                move_name = button.text.split(":")[0]
                                battle_text = f"{player_pokemon.name} used {move_name}!"
                                state = PLAYER_MOVE
                                if is_critical and not is_null:
                                    critical_hit_text = f"It's a critical hit!"
                                else:
                                    critical_hit_text = None
                                if is_effective:
                                    effective_text =  f"It's super effective!"
                                elif is_not_effective:
                                    effective_text =  f"It's not very effective..."
                                elif is_null:
                                    effective_text =  f"It had no effect!"
                                if ailment_applied:
                                    ailment_text = f" {opponent_pokemon.name} is {opponent_pokemon.status}!"
                                if stat_change_applied:
                                    stat_change_text = f" {player_pokemon.name} affected {target}'s stats!"
                                showing_moves = False
                
                if showing_items and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for button in item_buttons:
                        if button.check_click(mouse_pos):
                            battle_text = button.action()

                            if battle_text == f"You don't have any of this item":
                                state = PLAYER_TURN
                            else:
                                showing_items = False
                                state = PLAYER_MOVE
                            pygame.time.set_timer(pygame.USEREVENT, 2000)  # Set a timer for 2 seconds

                if showing_pokemon and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for button in pokemon_buttons:
                        if button.check_click(mouse_pos):
                            pokemon_choice = button.action()
                            if pokemon_choice == f"None":
                                state = PLAYER_TURN
                            else:
                                if player_pokemon.id != pokemon_choice.id:
                                    battle_text = f"Player switched to {pokemon_choice.name}!"
                                    player_pokemon = pokemon_choice
                                    player_pokemon_image = pygame.transform.scale(player_pokemon.image, (100, 100))  # Scale to 100x100 pixels
                                    showing_pokemon = False
                                    state = PLAYER_MOVE
                            pygame.time.set_timer(pygame.USEREVENT, 2000)  # Set a timer for 2 seconds
                            

            elif state == STATUS_CHECK:
                healed_status = random.random() < 0.5
                if healed_status:
                    if player_pokemon.status == "sleep":
                        player_pokemon.status = None
                        battle_text = f"{player_pokemon.name} woke up!"
                        showing_moves = True
                        state = PLAYER_TURN
                        pygame.time.set_timer(pygame.USEREVENT, 2000)  # Set a timer for 2 seconds
                    
                    elif player_pokemon.status == "confusion":
                        player_pokemon.status = None
                        battle_text = f"{player_pokemon.name} is no longer confused!"
                        showing_moves = True
                        state = PLAYER_TURN
                        pygame.time.set_timer(pygame.USEREVENT, 2000)
                    
                    elif player_pokemon.status == "freeze" :
                        player_pokemon.status = None
                        battle_text = f"{player_pokemon.name} thawed out!"
                        showing_moves = True
                        state = PLAYER_TURN
                        pygame.time.set_timer(pygame.USEREVENT, 2000)

                elif player_pokemon.status == "sleep":
                    state = PLAYER_MOVE
                    battle_text = f"{player_pokemon.name} is asleep and can't move!"
                    break
                
                elif player_pokemon.status == "confusion":
                    state = PLAYER_MOVE
                    battle_text = f"{player_pokemon.name} is confused and hurt itself!"
                    player_pokemon.take_damage(10)
                    break

                elif player_pokemon.status == "freeze":
                    state = PLAYER_MOVE
                    battle_text = f"{player_pokemon.name} is frozen solid and can't move!"
                    break

            elif state == PLAYER_MOVE:
                if critical_hit_text:
                    battle_text = critical_hit_text
                    critical_hit_text = None
                    state = PLAYER_MOVE
                    break
                if effective_text:
                    battle_text = effective_text
                    effective_text = None
                    state = PLAYER_MOVE
                    break
                if ailment_text:
                    battle_text = ailment_text
                    ailment_text = None
                    state = PLAYER_MOVE
                    break
                if stat_change_text:
                    battle_text = stat_change_text
                    stat_change_text = None
                    state = PLAYER_MOVE
                    break
                if num_hits_text:
                    battle_text = num_hits_text
                    num_hits_text = None
                    state = PLAYER_MOVE
                    break
                if player_pokemon.status == "poison" and poisonCheck:
                    poisonCheck = False
                    battle_text = f"{player_pokemon.name} is hurt by poison!"
                    player_pokemon.take_damage(player_pokemon.stats['hp'] // 8)
                    state = PLAYER_MOVE
                    break
                if player_pokemon.status == "burn" and burnCheck:
                    burnCheck = False
                    battle_text = f"{player_pokemon.name} is hurt by its burn!"
                    player_pokemon.take_damage(player_pokemon.stats['hp'] // 10)
                    state = PLAYER_MOVE
                    break
                else:
                    
                    poisonCheck = True
                    burnCheck = True
                    if not opponent_moved:
                        
                        state = OPPONENT_TURN
                        showing_moves = False
                        showing_items = False
                        battle_text = f"{opponent_pokemon.name}'s turn!"
                        player_moved = True
                        break
                    elif opponent_moved and  player_pokemon.stats["speed"] >= opponent_pokemon.stats["speed"]:
                        
                        state = PLAYER_TURN
                        battle_text = f"{player_pokemon.name}'s turn!"
                        opponent_moved = False
                        player_moved = True
                        break
                    else:
                        
                        state = OPPONENT_TURN
                        showing_moves = False
                        showing_items = False
                        battle_text = f"{opponent_pokemon.name}'s turn!"
                        player_moved = False
                        break

            elif state == OPPONENT_TURN:
                #check for status effects first
                if opponent_pokemon.status != "none" and opponent_pokemon.status != "paralysis":
                    opponent_healed_status = random.random() < 0.5
                    if opponent_healed_status:
                        if opponent_pokemon.status == "sleep":
                            battle_text = f"{opponent_pokemon.name} woke up!"
                            opponent_pokemon.status = "none"
                            state = OPPONENT_TURN
                            break
                        elif opponent_pokemon.status == "confusion":
                            battle_text = f"{opponent_pokemon.name} is no longer confused!"
                            opponent_pokemon.status = "none"
                            state = OPPONENT_TURN
                            break
                        elif opponent_pokemon.status == "freeze":
                            battle_text = f"{opponent_pokemon.name} thawed out!"
                            opponent_pokemon.status = "none"
                            state = OPPONENT_TURN
                            break
                    else:
                        if opponent_pokemon.status == "sleep":
                            battle_text = f"{opponent_pokemon.name} is asleep and can't move!"
                            state = OPPONENT_MOVE
                            break
                        elif opponent_pokemon.status == "confusion":
                            battle_text = f"{opponent_pokemon.name} is confused and hurt itself!"
                            opponent_pokemon.take_damage(10)
                            state = OPPONENT_MOVE
                            break
                        elif opponent_pokemon.status == "freeze":
                            battle_text = f"{opponent_pokemon.name} is frozen solid and can't move!"
                            state = OPPONENT_MOVE
                            break
                elif opponent_pokemon.status == "paralysis" and random.random() < 0.6:
                    battle_text = f"{opponent_pokemon.name} is paralyzed and can't move!"
                    state = OPPONENT_MOVE
                    break
                # Choose the best move based on type effectiveness and status
                best_move = None
                best_damage = 0
                for move in opponent_pokemon.moves:
                    if move['pp'] > 0:
                        # Calculate potential damage
                        damage = move['power'] * (opponent_pokemon.stats["attack"] if move['category'] == "physical" else opponent_pokemon.stats["special-attack"]) / (player_pokemon.stats["defense"] if move['category'] == "physical" else player_pokemon.stats["special-defense"])
                        if opponent_pokemon.type == move['type']:
                            damage *= 1.5
                        # Prioritize moves that are super effective or have status effects
                        if player_pokemon.type in pokemon_null[move['type']]:
                            continue
                        if player_pokemon.type in pokemon_advantages[move['type']]:
                            damage *= 2
                        elif player_pokemon.type in pokemon_disadvantages[move['type']]:
                            damage /= 2
                        if move['category'] == "status":
                            if opponent_pokemon.current_health >= opponent_pokemon.stats['hp'] and random.random() < 0.7:
                                best_move = move
                                break
                            damage = 0  # Status moves do not deal damage
                        if damage > best_damage:
                            best_damage = damage
                            best_move = move

                # If no move is selected, choose a random move
                if best_move is None:
                    best_move = random.choice([move for move in opponent_pokemon.moves if move['pp'] > 0])

                # Use the selected move
                damage, is_critical, is_effective, is_not_effective, is_null, ailment_applied, stat_change_applied, target, num_hits_text, missed = opponent_pokemon.use_move(best_move, player_pokemon)
                if missed:
                    battle_text = f"{opponent_pokemon.name} missed!"
                    state = OPPONENT_MOVE
                    break
                battle_text = f"{opponent_pokemon.name} used {best_move['name']} for {damage} damage!"
                state = OPPONENT_MOVE
                if is_critical and not is_null:
                    critical_hit_text = f"It's a critical hit!"
                else:
                    critical_hit_text = None
                if is_effective:
                    effective_text = f"It's super effective!"
                elif is_not_effective:
                    effective_text = f"It's not very effective..."
                elif is_null:
                    effective_text = f"It had no effect!"
                if ailment_applied:
                    ailment_text = f" {player_pokemon.name} is {player_pokemon.status}!"
                if stat_change_applied:
                    stat_change_text = f" {opponent_pokemon.name} affected {target}'s stats!"
                break

            elif state == OPPONENT_MOVE:
                if critical_hit_text:
                    battle_text = critical_hit_text
                    critical_hit_text = None
                    state = OPPONENT_MOVE
                    break
                if effective_text:
                    battle_text = effective_text
                    effective_text = None
                    state = OPPONENT_MOVE
                    break
                if ailment_text:
                    battle_text = ailment_text
                    ailment_text = None
                    state = OPPONENT_MOVE
                    break
                if stat_change_text:
                    battle_text = stat_change_text
                    stat_change_text = None
                    state = OPPONENT_MOVE
                    break
                if num_hits_text:
                    battle_text = num_hits_text
                    num_hits_text = None
                    state = OPPONENT_MOVE
                    break
                if opponent_pokemon.status == "poison" and poisonCheck:
                    poisonCheck = False
                    battle_text = f"{opponent_pokemon.name} is hurt by poison!"
                    opponent_pokemon.take_damage(opponent_pokemon.stats['hp'] // 8)
                    state = OPPONENT_MOVE
                    break
                if opponent_pokemon.status == "burn" and burnCheck:
                    burnCheck = False
                    battle_text = f"{opponent_pokemon.name} is hurt by its burn!"
                    opponent_pokemon.take_damage(opponent_pokemon.stats['hp'] // 10)
                    state = OPPONENT_MOVE
                    break
                else:
                    poisonCheck = True
                    burnCheck = True
                    if not player_moved:
                        state = PLAYER_TURN
                        battle_text = f"{player_pokemon.name}'s turn!"
                        opponent_moved = True
                        break
                    elif player_moved and  player_pokemon.stats["speed"] < opponent_pokemon.stats["speed"]:
                        state = OPPONENT_TURN
                        battle_text = f"{opponent_pokemon.name}'s turn!"
                        opponent_moved = True
                        player_moved = False
                        break
                    else:
                        state = PLAYER_TURN
                        battle_text = f"{player_pokemon.name}'s turn!"
                        opponent_moved = False
                        break

    return result # Return True if the player won, False if the player lost