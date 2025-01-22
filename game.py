"""
things to do:
- add new battle stages
- add legendary boss fights
- add game level system
- add way to see move info
- maybe set up turn system like in the games?
"""



import pygame
import random
from entities import Pokemon, Player, player
from battle import battle, Item, Button
from pokedex import pokedex
from inventory import display_buttons, create_item_buttons, create_pokemon_buttons, display_pokemon_buttons, create_pc_pokemon_buttons, display_pc_pokemon_buttons, move_pokemon_to_pc

pygame.init()


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 40  # Size of each tile (square)
GRID_WIDTH = SCREEN_WIDTH // TILE_SIZE  # Number of columns
GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE  # Number of rows
BATTLE_PROBABILITY = 0.1  # 10% chance of encountering a wild Pokémon

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 170, 249)
RED = (255, 0, 0)
DARK_RED = (139, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
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


#generate map
def generate_map(width, height):
    # 0 represents empty space, 1 represents walls
    map_data = [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]
    return map_data


# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PokeLeveling")

# Load tile images
grass_tile = pygame.transform.scale(pygame.image.load('Assets/Tiles/grass.png'), (TILE_SIZE, TILE_SIZE))
water_tile = pygame.transform.scale(pygame.image.load('Assets/Tiles/water.png'), (TILE_SIZE, TILE_SIZE))
fire_tile = pygame.transform.scale(pygame.image.load('Assets/Tiles/fire.png'), (TILE_SIZE, TILE_SIZE))
desert_tile = pygame.transform.scale(pygame.image.load('Assets/Tiles/sand.png'), (TILE_SIZE, TILE_SIZE))
snow_tile = pygame.transform.scale(pygame.image.load('Assets/Tiles/snow.png'), (TILE_SIZE, TILE_SIZE))
factory_tile = pygame.transform.scale(pygame.image.load('Assets/Tiles/factory.png'), (TILE_SIZE, TILE_SIZE))
graveyard_tile = pygame.transform.scale(pygame.image.load('Assets/Tiles/graveyard.png'), (TILE_SIZE, TILE_SIZE))
forest_tile = pygame.transform.scale(pygame.image.load('Assets/Tiles/forest.png'), (TILE_SIZE, TILE_SIZE))
dojo_tile = pygame.transform.scale(pygame.image.load('Assets/Tiles/dojo.png'), (TILE_SIZE, TILE_SIZE))
clouds_tile = pygame.transform.scale(pygame.image.load('Assets/Tiles/clouds.png'), (TILE_SIZE, TILE_SIZE))
swamp_tile = pygame.transform.scale(pygame.image.load('Assets/Tiles/swamp.png'), (TILE_SIZE, TILE_SIZE))
dragons_den_tile = pygame.transform.scale(pygame.image.load('Assets/Tiles/dragons_den.png'), (TILE_SIZE, TILE_SIZE))
# Define the different environments
environments = [grass_tile, water_tile, fire_tile, desert_tile, snow_tile, factory_tile, graveyard_tile, forest_tile, dojo_tile, clouds_tile, swamp_tile, dragons_den_tile]

# Define non-walkable tiles (e.g., water and fire tiles)
non_walkable_tiles = [
    pygame.Rect(11 * TILE_SIZE, 5 * TILE_SIZE, 9 * TILE_SIZE, 1 * TILE_SIZE),#beach boundary
    pygame.Rect(8 * TILE_SIZE, 0 * TILE_SIZE, 1 * TILE_SIZE, 6 * TILE_SIZE),#grass boundary
    pygame.Rect(8 * TILE_SIZE, 8 * TILE_SIZE, 1 * TILE_SIZE, 7 * TILE_SIZE),#fire boundary
    pygame.Rect(11 * TILE_SIZE, 8 * TILE_SIZE, 9 * TILE_SIZE, 1 * TILE_SIZE),#desert boundary
]

def is_walkable(x, y):
    for rect in non_walkable_tiles:
        if rect.collidepoint(x * TILE_SIZE, y * TILE_SIZE):
            return False
    return True

# Load and scale the background image
background_image = pygame.image.load('Assets/Background/background.png')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

#Load item menu image
item_menu = pygame.image.load('Assets/Background/item_menu.png')
item_menu = pygame.transform.scale(item_menu, (SCREEN_WIDTH, SCREEN_HEIGHT))

#load pc image
pc_menu = pygame.image.load('Assets/Background/pc_menu.png')
pc_menu = pygame.transform.scale(pc_menu, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Define regions with different sets of Pokémon
grassland = ["Turtwig", "Bulbasaur", "Eevee", "Jigglypuff", "Meowth", "Oddish", "Bellsprout", "Chikorita", "Treecko", "Slakoth"]
beach = ["Psyduck", "Squirtle", "Tentacool", "Slowpoke", "Krabby", "Sandygast", "Horsea", "Totodile", "Mudkip", "Piplup"]
volcano = ["Charmander", "Magby", "Slugma", "Darumaka", "Rolycoly", "Vulpix", "Growlithe", "Houndour", "Numel", "Torkoal"]
desert = ["Sandshrew", "Diglett", "Geodude", "Onix", "Sandile", "Trapinch", "Gible", "Roggenrola", "Nosepass", "Larvitar"]
snow = ["Snorunt", "Swinub", "Snom", "Vanillite", "Cubchoo", "Spheal", "Bergmite", "Sneasel", "Delibird", "Snover"]
factory = ["Magnemite", "Klink", "Porygon", "Rotom", "Aron", "Beldum", "Pawniard", "Honedge", "Klefki", "Meltan"]
graveyard = ["Gastly", "Shuppet", "Litwick", "Yamask", "Phantump", "Sableye", "Drifloon", "Duskull", "Spiritomb", "Misdreavus"]
forest = ["Caterpie", "Weedle", "Paras", "Venonat", "Pineco", "Shroomish", "Shelmet", "Kricketot", "Burmy", "Sewaddle"]
dojo = ["Hitmonlee", "Hitmonchan", "Hitmontop", "Machop", "Mankey", "Makuhita", "Riolu", "Throh", "Sawk", "Hawlucha"]
clouds = ["Pidgey", "Spearow", "Farfetchd", "Doduo", "Hoothoot", "Taillow", "Starly", "Pidove", "Aerodactyl", "Swablu"]
swamp = ["Zubat", "Grimer", "Koffing", "Croagunk", "Trubbish", "Venipede", "Skorupi", "Stunky", "Nidoran_f", "Nidoran_m"]
dragons_den = ["Dratini", "Bagon", "Axew", "Deino", "Druddigon"]

regions = {
    "grassland" : {"pokemon": random.sample(grassland, 5)},
    "beach" : {"pokemon": random.sample(beach, 5)},
    "volcano" : {"pokemon": random.sample(volcano, 5)},
    "desert" : {"pokemon": random.sample(desert, 5)},
    "snow" : {"pokemon": random.sample(snow, 5)},
    "factory" : {"pokemon": random.sample(factory, 5)},
    "graveyard" : {"pokemon": random.sample(graveyard, 5)},
    "forest" : {"pokemon": random.sample(forest, 5)},
    "dojo" : {"pokemon": random.sample(dojo, 5)},
    "clouds" : {"pokemon": random.sample(clouds, 5)},
    "swamp" : {"pokemon": random.sample(swamp, 5)},
    "dragons_den" : {"pokemon": random.sample(dragons_den, 5)}
}

regionsForDrawing = [
    {"encounter": pygame.Rect(0, 0, 8, 5),"rect": pygame.Rect(0, 0, 9 * TILE_SIZE, 6 * TILE_SIZE), "tile": random.choice(environments)},  # Top-left corner
    {"encounter": pygame.Rect(12, 0, 9, 5),"rect": pygame.Rect(11 * TILE_SIZE, 0, 9 * TILE_SIZE, 6 * TILE_SIZE), "tile": random.choice(environments)},  # Top-right corner
    {"encounter": pygame.Rect(0, 9, 8, 6),"rect": pygame.Rect(0, 8 * TILE_SIZE, 9 * TILE_SIZE, 7 * TILE_SIZE), "tile": random.choice(environments)},  # Bottom-left corner
    {"encounter": pygame.Rect(12, 9, 8, 6),"rect": pygame.Rect(11 * TILE_SIZE, 8 * TILE_SIZE, 9 * TILE_SIZE, 7 * TILE_SIZE), "tile": random.choice(environments)},  # Bottom-right corner
]

# get pokedex for this level
level_pokedex = []
level_areas = []
for region in regionsForDrawing:
    if region["tile"] not in level_areas:
        level_areas.append(region["tile"])
        if region["tile"] == grass_tile:
            level_pokedex += regions["grassland"]["pokemon"]
        elif region["tile"] == water_tile:
            level_pokedex += regions["beach"]["pokemon"]
        elif region["tile"] == fire_tile:
            level_pokedex += regions["volcano"]["pokemon"]
        elif region["tile"] == desert_tile:
            level_pokedex += regions["desert"]["pokemon"]
        elif region["tile"] == snow_tile:
            level_pokedex += regions["snow"]["pokemon"]
        elif region["tile"] == factory_tile:
            level_pokedex += regions["factory"]["pokemon"]
        elif region["tile"] == graveyard_tile:
            level_pokedex += regions["graveyard"]["pokemon"]
        elif region["tile"] == forest_tile:
            level_pokedex += regions["forest"]["pokemon"]
        elif region["tile"] == dojo_tile:
            level_pokedex += regions["dojo"]["pokemon"]
        elif region["tile"] == clouds_tile:
            level_pokedex += regions["clouds"]["pokemon"]
        elif region["tile"] == swamp_tile:
            level_pokedex += regions["swamp"]["pokemon"]
        elif region["tile"] == dragons_den_tile:
            level_pokedex += regions["dragons_den"]["pokemon"]

# figur eout which corner is which
corners = []
for region in regionsForDrawing:
    if region["tile"] == grass_tile:
        corners.append("grassland")
    elif region["tile"] == water_tile:
        corners.append("beach")
    elif region["tile"] == fire_tile:
        corners.append("volcano")
    elif region["tile"] == desert_tile:
        corners.append("desert")
    elif region["tile"] == snow_tile:
        corners.append("snow")
    elif region["tile"] == factory_tile:
        corners.append("factory")
    elif region["tile"] == graveyard_tile:
        corners.append("graveyard")
    elif region["tile"] == forest_tile:
        corners.append("forest")
    elif region["tile"] == dojo_tile:
        corners.append("dojo")
    elif region["tile"] == clouds_tile:
        corners.append("clouds")
    elif region["tile"] == swamp_tile:
        corners.append("swamp")
    elif region["tile"] == dragons_den_tile:
        corners.append("dragons_den")

# Load foreground images
top_left_corner = pygame.image.load(f'Assets/Background/Foreground/{corners[0]}_top_left.png')
top_right_corner = pygame.image.load(f'Assets/Background/Foreground/{corners[1]}_top_right.png')
bottom_left_corner = pygame.image.load(f'Assets/Background/Foreground/{corners[2]}_bottom_left.png')
bottom_right_corner = pygame.image.load(f'Assets/Background/Foreground/{corners[3]}_bottom_right.png')

#scale foreground images
top_left_corner = pygame.transform.scale(top_left_corner, (9 * TILE_SIZE, 6 * TILE_SIZE))
top_right_corner = pygame.transform.scale(top_right_corner, (9 * TILE_SIZE, 6 * TILE_SIZE))
bottom_left_corner = pygame.transform.scale(bottom_left_corner, (9 * TILE_SIZE, 7 * TILE_SIZE))
bottom_right_corner = pygame.transform.scale(bottom_right_corner, (9 * TILE_SIZE, 7 * TILE_SIZE))


def draw_regions(screen):
    for region in regionsForDrawing:
        tile = region["tile"]
        rect = region["rect"]
        for x in range(rect.left, rect.right, TILE_SIZE):
            for y in range(rect.top, rect.bottom, TILE_SIZE):
                screen.blit(tile, (x, y))


def get_region_pokemon(player_x, player_y):
    for region in regionsForDrawing:
        if region["encounter"].collidepoint(player_x, player_y):
            if region["tile"] == grass_tile:
                return regions["grassland"]["pokemon"]
            elif region["tile"] == water_tile:
                return regions["beach"]["pokemon"]
            elif region["tile"] == fire_tile:
                return regions["volcano"]["pokemon"]
            elif region["tile"] == desert_tile:
                return regions["desert"]["pokemon"]
            elif region["tile"] == snow_tile:
                return regions["snow"]["pokemon"]
            elif region["tile"] == factory_tile:
                return regions["factory"]["pokemon"]
            elif region["tile"] == graveyard_tile:
                return regions["graveyard"]["pokemon"]
            elif region["tile"] == forest_tile:
                return regions["forest"]["pokemon"]
            elif region["tile"] == dojo_tile:
                return regions["dojo"]["pokemon"]
            elif region["tile"] == clouds_tile:
                return regions["clouds"]["pokemon"]
            elif region["tile"] == swamp_tile:
                return regions["swamp"]["pokemon"]
            elif region["tile"] == dragons_den_tile:
                return regions["dragons_den"]["pokemon"]
    return []  # Default to an empty list if no region matches

def get_player_pokedex_completion(pokedex_complete, player):
    pokedex_completion = 0
    for pokemon in set(player.pokemon_team):
        if pokemon.name in level_pokedex:
            pokedex_completion += 1
            pokedex[pokemon.name].caught = True
    for pokemon in set(player.pc):
        if pokemon.name in level_pokedex:
            pokedex_completion += 1
            pokedex[pokemon.name].caught = True

    return pokedex_completion

# Define a list of starter Pokémon
starter_pokemon = ["Bulbasaur", "Charmander", "Squirtle"]

# Create buttons for each starter Pokémon
starter_buttons = []
for i, pokemon in enumerate(starter_pokemon):
    starter_buttons.append(Button(
        100, 100 + 70 * i, 200, 50,
        pokemon, pygame.font.Font(None, 25), WHITE, BLACK,
        lambda pokemon=pokemon: select_starter(pokemon), BLACK
    ))

def select_starter(pokemon_name):
    player.pokemon_team.append(pokedex[pokemon_name])
    global starter_selected
    starter_selected = True

#def starter menu image
starter_menu = pygame.image.load('Assets/Background/starter_menu.png')
#scale starter menu image
starter_menu = pygame.transform.scale(starter_menu, (SCREEN_WIDTH, SCREEN_HEIGHT))
#starter menu text
starter_menu_text = pygame.font.Font(None, 36).render("Choose your starter Pokémon", True, BLACK)
starter_menu_text_rect = starter_menu_text.get_rect(center=(SCREEN_WIDTH // 2, 40))

# Main game loop
starter_selected = False
pokedex_complete = False
font = pygame.font.Font(None, 22)
prev_x, prev_y = player.grid_x, player.grid_y
running = True
moving = False
direction = "down"
item_buttons = create_item_buttons(player, screen, SCREEN_WIDTH)
pokemon_buttons = create_pokemon_buttons(screen)
inventory_open = False
move_to_pc_button = Button(740, 10, 50, 50, "PC", font, DARK_GREEN, WHITE, lambda: False, BLACK)
pc_open = False
page = 0
next_page_button = Button(740, 10, 50, 25, "Next", font, DARK_GREEN, WHITE, lambda: False, BLACK)
prev_page_button = Button(10, 10, 50, 25, "Prev", font, DARK_GREEN, WHITE, lambda: False, BLACK)
pc_pokemon_buttons = create_pc_pokemon_buttons(screen, player, SCREEN_WIDTH, page)
item = None
selected = Button(0, 0, 0, 0, "", None, None, None, None, None)
selected_pokemon = None
item_description = "Use an item or move pokemon"
pc_description = "Move pokemon to team"
winBattle = False
rewards_display_time = 3000  # Time in milliseconds to display the rewards text
rewards_start_time = None
pokedex_completion = get_player_pokedex_completion(pokedex_complete, player)
while running:
    if not starter_selected:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in starter_buttons:
                    if button.check_click(event.pos):
                        button.action()
                        pokemon_buttons = create_pokemon_buttons(screen)

        screen.fill(LIGHT_BLUE)
        screen.blit(starter_menu, (0, 0))
        screen.blit(starter_menu_text, starter_menu_text_rect)
        
        # Display starter selection screen
        for button in starter_buttons:
            button.draw(screen)
        # Handle button hover
        mouse_pos = pygame.mouse.get_pos()
        for button in starter_buttons:
            button.check_hover(mouse_pos)
        pygame.display.flip()
    else:
        # Reset the screen
        screen.fill(WHITE)
        

        # Draw the regions
        draw_regions(screen)

        # Draw the background/foreground image
        screen.blit(background_image, (0, 0))
        screen.blit(top_left_corner, (0, 0))
        screen.blit(top_right_corner, (11 * TILE_SIZE, 0))
        screen.blit(bottom_left_corner, (0, 8 * TILE_SIZE))
        screen.blit(bottom_right_corner, (11 * TILE_SIZE, 8 * TILE_SIZE))


        # Draw the player
        player.draw(screen, TILE_SIZE)

        #display pokedex completion
        pokedex_completion_text = f"{pokedex_completion}/{len(level_pokedex)}"
        pokedex_completion_text_surface = pygame.font.Font(None, 30).render(pokedex_completion_text, True, BLACK)
        pokedex_completion_text_rect = pokedex_completion_text_surface.get_rect(center=(screen.get_width() // 2, 10))
        screen.blit(pokedex_completion_text_surface, pokedex_completion_text_rect)

    # Handle events (such as closing the game window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pc_open = False
                inventory_open = not inventory_open
                item_description = "Use an item or move pokemon"
                selected_pokemon = None
                item = None
                selected = Button(0, 0, 0, 0, "", None, None, None, None, None)
            elif event.key == pygame.K_e:
                pc_description = "Move pokemon to team"
                inventory_open = False
                pc_open = not pc_open
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and pc_open:
            mouse_pos = pygame.mouse.get_pos()
            # Check if a pc pokemon button is clicked
            for button in pc_pokemon_buttons:
                if button.rect.collidepoint(mouse_pos):
                    pc_description = button.action()
                    pc_pokemon_buttons = create_pc_pokemon_buttons(screen, player, SCREEN_WIDTH, page)
                    pokemon_buttons = create_pokemon_buttons(screen)
            #check if player moved pages
            if next_page_button.rect.collidepoint(mouse_pos):
                if (page + 1) * 21 < len(player.pc):
                    page += 1
                    pc_pokemon_buttons = create_pc_pokemon_buttons(screen, player, SCREEN_WIDTH, page)
            elif prev_page_button.rect.collidepoint(mouse_pos):
                if page > 0:
                    page -= 1
                    pc_pokemon_buttons = create_pc_pokemon_buttons(screen, player, SCREEN_WIDTH, page)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and inventory_open:
            mouse_pos = pygame.mouse.get_pos()
            # Check if an item button is clicked
            for button in item_buttons:
                if button.rect.collidepoint(mouse_pos):
                    item = button.action()
                    selected = button
                    selected_pokemon = None
            
            if item:
                for button in pokemon_buttons:
                    if button.rect.collidepoint(mouse_pos):
                        pokemon_id, pokemon_moves = button.action()
                        for i, pokemon in enumerate(player.pokemon_team):
                            if pokemon.id == pokemon_id:
                                pokemon_name = player.pokemon_team[i]
                                break
                        item_description = player.use_item(item, pokemon_name)
                        # Update the buttons with the new HP and item amnts
                        pokemon_buttons = create_pokemon_buttons(screen)
                        selected_pokemon = None
                        item_buttons = create_item_buttons(player, screen, SCREEN_WIDTH)
                        item = None
            else:
                for button in pokemon_buttons:
                    if button.rect.collidepoint(mouse_pos):
                        pokemon_id, pokemon_moves = button.action()
                        selected = button
                        for i, pokemon in enumerate(player.pokemon_team):
                            if pokemon.id == pokemon_id:
                                if selected_pokemon is None:
                                    selected_pokemon = i
                                else:
                                    # Swap the selected Pokémon with the current one
                                    player.pokemon_team[selected_pokemon], player.pokemon_team[i] = player.pokemon_team[i], player.pokemon_team[selected_pokemon]
                                    item_description = f"Swapped {player.pokemon_team[selected_pokemon].name} with {player.pokemon_team[i].name}"
                                    selected_pokemon = None
                                    item = None
                                    pokemon_buttons = create_pokemon_buttons(screen)
                                break
                if move_to_pc_button.rect.collidepoint(mouse_pos) and selected_pokemon is not None:
                    item_description = move_pokemon_to_pc(player, player.pokemon_team[selected_pokemon])
                    pokemon_buttons = create_pokemon_buttons(screen)
                    pc_pokemon_buttons = create_pc_pokemon_buttons(screen, player, SCREEN_WIDTH, page)
                    selected_pokemon = None
                    item = None

    
    if inventory_open:
        selected.border_color = LIGHT_BLUE
        for button in pokemon_buttons:
                if button != selected:
                    button.border_color = BLACK
        for button in item_buttons:
                if button != selected:
                    button.border_color = BLACK
        screen.fill(WHITE)
        screen.blit(item_menu, (0, 0))
        display_buttons(screen, player, item_buttons)
        display_pokemon_buttons(screen, player, pokemon_buttons)
        move_to_pc_button.draw(screen)
        move_to_pc_button.check_hover(pygame.mouse.get_pos())
        # Display item description
        item_description_surface = font.render(item_description, True, (0, 0, 0))
        item_description_rect = item_description_surface.get_rect(center=(screen.get_width() // 4, 550))
        screen.blit(item_description_surface, item_description_rect)
    elif pc_open:
        screen.fill(WHITE)
        screen.blit(pc_menu, (0, 0))
        display_pc_pokemon_buttons(screen, player, pc_pokemon_buttons)
        next_page_button.draw(screen)
        next_page_button.check_hover(pygame.mouse.get_pos())
        prev_page_button.draw(screen)
        prev_page_button.check_hover(pygame.mouse.get_pos())
        # Display pc description
        pc_description_surface = font.render(pc_description, True, (0, 0, 0))
        pc_description_rect = pc_description_surface.get_rect(center=(screen.get_width() // 2, 575))
        screen.blit(pc_description_surface, pc_description_rect)
    else:

        # Handle key press events for movement
        keys = pygame.key.get_pressed()

        # To prevent diagonal movement, only allow one direction at a time.
        dx = 0
        dy = 0

        # Horizontal movement (left or right)
        if keys[pygame.K_a]:
            if direction == "left":
                dx = -1
                player.image = [pygame.image.load(f'Assets\\Player\\player_walking_left{i}.png') for i in range(1, 5)]
                moving = True
            else:
                player.image = [pygame.image.load(f'Assets\\Player\\player_walking_left1.png')]
                direction = "left"
        elif keys[pygame.K_d]:
            if direction == "right":
                dx = 1
                player.image = [pygame.image.load(f'Assets\\Player\\player_walking_right{i}.png') for i in range(1, 5)]
                moving = True
            else:
                player.image = [pygame.image.load(f'Assets\\Player\\player_walking_right1.png')]
                direction = "right"

        # Vertical movement (up or down)
        elif keys[pygame.K_w]:
            if direction == "up":
                dy = -1
                player.image = [pygame.image.load(f'Assets\\Player\\player_walking_up{i}.png') for i in range(1, 5)]
                moving = True
            else:
                player.image = [pygame.image.load(f'Assets\\Player\\player_walking_up1.png')]
                direction = "up"
        elif keys[pygame.K_s]:
            if direction == "down":
                dy = 1
                player.image = [pygame.image.load(f'Assets\\Player\\player_walking_down{i}.png') for i in range(1, 5)]
                moving = True
            else:
                player.image = [pygame.image.load(f'Assets\\Player\\player_walking_down1.png')]
                direction = "down"
        else:
            moving = False
            player.frame = 0

        # Move the player based on the dx and dy if the tile is walkable
        if is_walkable(player.grid_x + dx, player.grid_y + dy):
            player.move(dx, dy, GRID_WIDTH, GRID_HEIGHT)

        # Check if the player stepped on a tile that triggers a battle
        if (player.grid_x, player.grid_y) != (prev_x, prev_y):
            # Update previous position
            prev_x, prev_y = player.grid_x, player.grid_y
            
            # Get the set of Pokémon for the current region
            region_pokemon = get_region_pokemon(player.grid_x, player.grid_y)

            # Start the battle if the random number is within the encounter probability
            if random.random() < BATTLE_PROBABILITY and len(region_pokemon)>0:
                opponent_pokemon_name = random.choice(region_pokemon)
                opponent_pokemon = pokedex[opponent_pokemon_name]
                lvlDiff = random.randint(-3, 2)
                environment = (regionsForDrawing[i]["tile"] for i in range(len(regionsForDrawing)) if regionsForDrawing[i]["rect"].collidepoint(player.grid_x * TILE_SIZE, player.grid_y * TILE_SIZE)).__next__()
                battle_stage = (i + 1 for i in range(len(environments)) if environments[i] == environment).__next__()
                print(opponent_pokemon.moves)
                winBattle = battle(screen, SCREEN_WIDTH, SCREEN_HEIGHT, battle_stage, player.pokemon_team[0], Pokemon(opponent_pokemon.name, opponent_pokemon.type, max(1, player.pokemon_team[0].level + lvlDiff), opponent_pokemon.moves, is_wild=True))
                pokemon_buttons = create_pokemon_buttons(screen)
                item_buttons = create_item_buttons(player, screen, SCREEN_WIDTH)
                pc_pokemon_buttons = create_pc_pokemon_buttons(screen, player, SCREEN_WIDTH, page)
            if winBattle:
                # get player known pokedex
                pokedex_completion = get_player_pokedex_completion(pokedex_complete, player)
                    
                for pokemon in level_pokedex:
                    if not pokedex[pokemon].caught:
                        pokedex_complete = False
                        break
                    else:
                        pokedex_complete = True
                
                if pokedex_complete:
                    rewards_text = f"Player completed the Pokédex!"
                    rewards_text_surface = pygame.font.Font(None, 60).render(rewards_text, True, RED)
                    rewards_text_rect = rewards_text_surface.get_rect(center=(screen.get_width() // 2, 277))
                    rewards_start_time = pygame.time.get_ticks()
                
                else:  
                    for item in player.inventory:
                        player.inventory[item] += 1
                    item_buttons = create_item_buttons(player, screen, SCREEN_WIDTH)
                    rewards_text = f"Player restocked items!"
                    rewards_text_surface = pygame.font.Font(None, 30).render(rewards_text, True, RED)
                    rewards_text_rect = rewards_text_surface.get_rect(center=(screen.get_width() // 2, 277))
                    rewards_start_time = pygame.time.get_ticks()  # Start the timer
                    winBattle = False

        # Display the rewards text if the timer is running
        if rewards_start_time:
            current_time = pygame.time.get_ticks()
            if current_time - rewards_start_time < rewards_display_time:
                screen.blit(rewards_text_surface, rewards_text_rect)
            else:
                rewards_start_time = None  # Reset the timer

        #if moving update player frame
        #update player frame
        if moving:
            player.update_frame()

    

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    pygame.time.Clock().tick(10)

# Quit Pygame
pygame.quit()
