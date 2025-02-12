import requests
import json
import os
from uuid import UUID

# File path for the cache
move_file = 'move_cache.json'
stats_file = 'stats_cache.json'
learnable_moves_file = 'learnable_moves_cache.json'

ailments = ["burn", "freeze", "paralysis", "poison", "sleep", "confusion", "trap", "none"]

# Function to load the cache from a file
def load_cache(cache_file):
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            return json.load(f)
    return {}

# Function to save the cache to a file
def save_cache(cache_data, file):
    with open(file, 'w') as f:
        json.dump(cache_data, f)

# Function to get move data (with caching)
def get_move_data(move_name):
    if not isinstance(move_name, str):
        return move_name

    # Load cache from file
    cache = load_cache(move_file)

    # Check if move data is already cached
    if move_name in cache:
        return cache[move_name]
    
    # Fetch data from PokeAPI if not cached
    url = f"https://pokeapi.co/api/v2/move/{move_name}/"
    response = requests.get(url)
    
    # Check if the response is valid JSON
    try:
        move_data = response.json()
    except requests.exceptions.JSONDecodeError:
        print(f"Error: Failed to fetch data for move '{move_name}'")
        return None

    # Extract only the relevant information
    move_info = {
        "name": move_data["name"],
        "power": move_data.get("power") if move_data.get("power") is not None else 0,  # Some moves may not have power
        "max_pp": move_data.get("pp", 0),  # Kepp track of max pp
        "pp": move_data.get("pp", 0),  # Some moves may not have pp
        "category": move_data["damage_class"]["name"],
        "type": move_data["type"]["name"],
        "crit_chance": move_data["meta"]["crit_rate"] if move_data["meta"] is not None else 0,
        "effect_chance": move_data["effect_chance"] if move_data["effect_chance"] is not None else 0,
        "ailment": move_data["meta"]["ailment"]["name"] if move_data["meta"] and move_data["meta"]["ailment"]["name"] is not None else "none",
        "stat_changes": move_data["stat_changes"],
        "min_hits": move_data["meta"]["min_hits"] if move_data["meta"] and move_data["meta"]["min_hits"] is not None else 1,
        "max_hits": move_data["meta"]["max_hits"] if move_data["meta"] and move_data["meta"]["max_hits"] is not None else 1,
        "effect": move_data["effect_entries"][0]["short_effect"] if move_data["effect_entries"] else "None",
    }

    # Filter out moves with complicated effects
    if move_info["ailment"] not in ailments or move_info['category'] != "status" and move_info['power'] == 0:
        # Cache the move data
        cache[move_name] = 0
        save_cache(cache, move_file)

        return 0

    # Cache the move data
    cache[move_name] = move_info
    save_cache(cache, move_file)

    return move_info

def get_pokemon_stats(pokemon_name):
    # Load cache from file
    cache = load_cache(stats_file)

    # Check if move data is already cached
    if pokemon_name in cache:
        return cache[pokemon_name]
    
    # Fetch data from PokeAPI if not cached
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
    response = requests.get(url)
    
    # Check if the response is valid JSON
    try:
        pokemon_data = response.json()
    except requests.exceptions.JSONDecodeError:
        print(f"Error: Failed to fetch data for pokemon '{pokemon_name}'")
        return None

    # Extract only the relevant information
    pokemon_info = {}

    for stat in pokemon_data["stats"]:
        stat_name = stat["stat"]["name"]
        stat_value = stat["base_stat"]
        pokemon_info[stat_name] = stat_value
    pokemon_info["accuracy"] = 100
    pokemon_info["evasion"] = 100

    # Cache the move data
    cache[pokemon_name] = pokemon_info
    save_cache(cache, stats_file)

    return pokemon_info

def get_pokemon_moves(pokemon_name):
    # Load cache from file
    cache = load_cache(learnable_moves_file)

    # Check if move data is already cached
    if pokemon_name in cache:
        return cache[pokemon_name]
    
    # Fetch data from PokeAPI if not cached
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
    response = requests.get(url)
    
    # Check if the response is valid JSON
    try:
        pokemon_data = response.json()
    except requests.exceptions.JSONDecodeError:
        print(f"Error: Failed to fetch learnable moves for pokemon '{pokemon_name}'")
        return None

    # Extract only the relevant information
    pokemon_info = []

    for move in pokemon_data["moves"]:
        move_info = get_move_data(move["move"]["name"])
        if move_info == 0:
            continue
        if move_info["ailment"] not in ailments or move_info['category'] != "status" and move_info['power'] == 0:
            continue
        pokemon_info.append(move["move"]["name"])

    # Cache the move data
    cache[pokemon_name] = pokemon_info
    save_cache(cache, learnable_moves_file)

    return pokemon_info

#save player data function
def save_player_data(player, map_data):
    def convert_uuid_to_str(data):
        if isinstance(data, dict):
            return {key: convert_uuid_to_str(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [convert_uuid_to_str(item) for item in data]
        elif isinstance(data, UUID):
            return str(data)
        else:
            return data

    data = {
        "pokemon_team": [convert_uuid_to_str(pokemon.__dict__) for pokemon in player.pokemon_team],
        "inventory": convert_uuid_to_str(player.inventory),
        "pc": [convert_uuid_to_str(pokemon.__dict__) for pokemon in player.pc],
        "regions": map_data
    }
    with open("player_data.json", "w") as file:
        json.dump(data, file, indent=4)


