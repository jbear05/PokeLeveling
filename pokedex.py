from entities import Pokemon
import random

pokedex = {
    # Electric type Pokémon
    "Pikachu": Pokemon("Pikachu", "electric", 5, ["quick-attack", "thunder-shock"], "Raichu", 20),

    "Raichu": Pokemon("Raichu", "electric", 1, ["quick-attack", "thunder-shock"]),

    "Rotom": Pokemon("Rotom", "electric", 5, ["thunder-shock", "astonish"]),

    "Magnemite": Pokemon("Magnemite", "electric", 5, ["tackle", "thunder-shock"], "Magneton", 30),

    "Magneton": Pokemon("Magneton", "electric", 1, ["tackle", "thunder-shock"], "Magnezone", 40),

    "Magnezone": Pokemon("Magnezone", "electric", 1, ["tackle", "thunder-shock"]),

    # Grass type Pokémon
    "Bulbasaur": Pokemon("Bulbasaur", "grass", 5, ["tackle", "vine-whip"], "Ivysaur", 16),

    "Ivysaur": Pokemon("Ivysaur", "grass", 1, ["tackle", "vine-whip"], "Venusaur", 32),

    "Venusaur": Pokemon("Venusaur", "grass", 1, ["tackle", "vine-whip"]),

    "Oddish": Pokemon("Oddish", "grass", 5, ["absorb", "acid"], "Gloom", 21),

    "Gloom": Pokemon("Gloom", "grass", 1, ["absorb", "acid"], "Vileplume", 32),

    "Vileplume": Pokemon("Vileplume", "grass", 1, ["absorb", "acid"]),

    "Bellsprout": Pokemon("Bellsprout", "grass", 5, ["vine-whip", "acid"], "Weepinbell", 21),

    "Weepinbell": Pokemon("Weepinbell", "grass", 1, ["vine-whip", "acid"], "Victreebel", 32),

    "Victreebel": Pokemon("Victreebel", "grass", 1, ["vine-whip", "acid"]),

    "Chikorita": Pokemon("Chikorita", "grass", 5, ["tackle", "razor-leaf"], "Bayleef", 16),

    "Bayleef": Pokemon("Bayleef", "grass", 1, ["tackle", "razor-leaf"], "Meganium", 32),

    "Meganium": Pokemon("Meganium", "grass", 1, ["tackle", "razor-leaf"]),

    "Treecko": Pokemon("Treecko", "grass", 5, ["scratch", "absorb"], "Grovyle", 16),

    "Grovyle": Pokemon("Grovyle", "grass", 1, ["quick-attack", "absorb"], "Sceptile", 36),

    "Turtwig": Pokemon("Turtwig", "grass", 5, ["tackle", "absorb"], "Grotle", 18),

    "Grotle": Pokemon("Grotle", "grass", 1, ["tackle", "absorb"], "Torterra", 32),

    "Torterra": Pokemon("Torterra", "grass", 1, ["tackle", "absorb"]),

    "Shroomish": Pokemon("Shroomish", "grass", 5, ["absorb", "tackle"], "Breloom", 23),

    "Breloom": Pokemon("Breloom", "grass", 1, ["absorb", "tackle"]),

    # Fire type Pokémon
    "Charmander": Pokemon("Charmander", "fire", 5, ["tackle", "ember"], "Charmeleon", 16),

    "Charmeleon": Pokemon("Charmeleon", "fire", 1, ["tackle", "ember"], "Charizard", 36),

    "Charizard": Pokemon("Charizard", "fire", 1, ["tackle", "ember"]),
    
    "Magby": Pokemon("Magby", "fire", 5, ["tackle", "ember"], "Magmar", 30),

    "Magmar": Pokemon("Magmar", "fire", 1, ["tackle", "ember"], "Magmortar", 40),

    "Magmortar": Pokemon("Magmortar", "fire", 1, ["tackle", "ember"]),
    
    "Slugma": Pokemon("Slugma", "fire", 5, ["tackle", "ember"], "Magcargo", 38),

    "Magcargo": Pokemon("Magcargo", "fire", 1, ["tackle", "ember"]),
    
    "Darumaka": Pokemon("Darumaka", "fire", 5, ["scratch", "ember"], "Darmanitan", 35),

    "Darmanitan": Pokemon("Darmanitan", "fire", 1, ["scratch", "ember"]),
    
    "Rolycoly": Pokemon("Rolycoly", "fire", 5, ["scratch", "ember"], "Carkol", 18),

    "Carkol": Pokemon("Carkol", "fire", 1, ["scratch", "ember"], "Coalossal", 34),

    "Coalossal": Pokemon("Coalossal", "fire", 1, ["scratch", "ember"]),

    "Vulpix": Pokemon("Vulpix", "fire", 5, ["ember", "quick-attack"], "Ninetales", 30),

    "Ninetales": Pokemon("Ninetales", "fire", 1, ["ember", "quick-attack"]),
    
    "Growlithe": Pokemon("Growlithe", "fire", 5, ["bite", "ember"], "Arcanine", 30),

    "Arcanine": Pokemon("Arcanine", "fire", 1, ["bite", "ember"]),
    
    "Houndour": Pokemon("Houndour", "fire", 5, ["ember", "leer"], "Houndoom", 24),

    "Houndoom": Pokemon("Houndoom", "fire", 1, ["ember", "leer"]),
    
    "Numel": Pokemon("Numel", "fire", 5, ["tackle", "growl"], "Camerupt", 33),

    "Camerupt": Pokemon("Camerupt", "fire", 1, ["tackle", "growl"]),
    
    "Torkoal": Pokemon("Torkoal", "fire", 5, ["ember", "withdraw"]),

    # Water type Pokémon
    "Squirtle": Pokemon("Squirtle", "water", 5, ["tackle", "water-gun"], "Wartortle", 16),

    "Wartortle": Pokemon("Wartortle", "water", 1, ["tackle", "water-gun"], "Blastoise", 36),

    "Blastoise": Pokemon("Blastoise", "water", 1, ["tackle", "water-gun"]),
    
    "Psyduck": Pokemon("Psyduck", "water", 5, ["scratch", "water-gun"], "Golduck", 33),

    "Golduck": Pokemon("Golduck", "water", 1, ["scratch", "water-gun"]),
    
    "Tentacool": Pokemon("Tentacool", "water", 5, ["scratch", "wrap"], "Tentacruel", 30),

    "Tentacruel": Pokemon("Tentacruel", "water", 1, ["scratch", "wrap"]),
    
    "Slowpoke": Pokemon("Slowpoke", "water", 5, ["confusion", "water-gun"], "Slowbro", 37),

    "Slowbro": Pokemon("Slowbro", "water", 1, ["confusion", "water-gun"]),
    
    "Krabby": Pokemon("Krabby", "water", 5, ["scratch", "water-gun"], "Kingler", 28),

    "Kingler": Pokemon("Kingler", "water", 1, ["scratch", "water-gun"]),

    "Horsea": Pokemon("Horsea", "water", 5, ["bubble", "water-gun"], "Seadra", 32),

    "Seadra": Pokemon("Seadra", "water", 1, ["bubble", "water-gun"], "Kingdra", 40),

    "Kingdra": Pokemon("Kingdra", "water", 1, ["bubble", "water-gun"]),

    "Totodile": Pokemon("Totodile", "water", 5, ["scratch", "water-gun"], "Croconaw", 18),

    "Croconaw": Pokemon("Croconaw", "water", 1, ["scratch", "water-gun"], "Feraligatr", 30),

    "Feraligatr": Pokemon("Feraligatr", "water", 1, ["scratch", "water-gun"]),

    "Mudkip": Pokemon("Mudkip", "water", 5, ["tackle", "water-gun"], "Marshtomp", 16),

    "Marshtomp": Pokemon("Marshtomp", "water", 1, ["tackle", "water-gun"], "Swampert", 36),

    "Swampert": Pokemon("Swampert", "water", 1, ["tackle", "water-gun"]),

    "Piplup": Pokemon("Piplup", "water", 5, ["scratch", "bubble"], "Prinplup", 16),

    "Prinplup": Pokemon("Prinplup", "water", 1, ["scratch", "bubble"], "Empoleon", 36),

    "Empoleon": Pokemon("Empoleon", "water", 1, ["scratch", "bubble"]),

    # Normal type Pokémon
    "Eevee": Pokemon("Eevee", "normal", 5, ["tackle", "swift"], random.choice["Vaporeon", "Jolteon", "Flareon", "Espeon", "Umbreon", "Leafeon", "Glaceon", "Sylveon"], 20),
    
    "Jigglypuff": Pokemon("Jigglypuff", "normal", 5, ["tackle", "sing"], "Wigglytuff", 30),

    "Wigglytuff": Pokemon("Wigglytuff", "normal", 1, ["tackle", "sing"]),
    
    "Meowth": Pokemon("Meowth", "normal", 5, ["scratch", "pay-day"], "Persian", 28),

    "Persian": Pokemon("Persian", "normal", 1, ["scratch", "pay-day"]),

    "Slakoth": Pokemon("Slakoth", "normal", 5, ["scratch", "yawn"], "Vigoroth", 18),

    "Vigoroth": Pokemon("Vigoroth", "normal", 1, ["scratch", "yawn"], "Slaking", 36),

    "Slaking": Pokemon("Slaking", "normal", 1, ["scratch", "yawn"]),

    # Ground type Pokémon
    "Sandshrew": Pokemon("Sandshrew", "ground", 5, ["scratch", "mud-slap"], "Sandslash", 22),

    "Sandslash": Pokemon("Sandslash", "ground", 1, ["scratch", "mud-slap"]),
    
    "Diglett": Pokemon("Diglett", "ground", 5, ["dig", "tackle"], "Dugtrio", 26),

    "Dugtrio": Pokemon("Dugtrio", "ground", 1, ["dig", "tackle"]),
    
    "Sandile": Pokemon("Sandile", "ground", 5, ["mud-slap", "tackle"], "Krokorok", 29),

    "Krokorok": Pokemon("Krokorok", "ground", 1, ["mud-slap", "tackle"], "Krookodile", 40),

    "Krookodile": Pokemon("Krookodile", "ground", 1, ["mud-slap", "tackle"]),

    "Trapinch": Pokemon("Trapinch", "ground", 5, ["bite"], "Vibrava", 35),

    "Vibrava": Pokemon("Vibrava", "ground", 1, ["bite"], "Flygon", 45),

    "Flygon": Pokemon("Flygon", "ground", 1, ["bite"]),

    "Gible": Pokemon("Gible", "ground", 5, ["tackle"], "Gabite", 24),

    "Gabite": Pokemon("Gabite", "ground", 1, ["tackle"], "Garchomp", 48),

    "Garchomp": Pokemon("Garchomp", "ground", 1, ["tackle"]),

    # Rock type Pokémon
    "Geodude": Pokemon("Geodude", "rock", 5, ["tackle", "rock-throw"], "Graveler", 25),

    "Graveler": Pokemon("Graveler", "rock", 1, ["tackle", "rock-throw"], "Golem", 40),

    "Golem": Pokemon("Golem", "rock", 1, ["tackle", "rock-throw"]),
    
    "Onix": Pokemon("Onix", "rock", 5, ["tackle", "rock-throw"], "Steelix", 40),

    "Steelix": Pokemon("Steelix", "rock", 1, ["tackle", "rock-throw"]),

    "Roggenrola": Pokemon("Roggenrola", "rock", 5, ["tackle", "rock-throw"], "Boldore", 25),

    "Boldore": Pokemon("Boldore", "rock", 1, ["tackle", "rock-throw"], "Gigalith", 40),

    "Gigalith": Pokemon("Gigalith", "rock", 1, ["tackle", "rock-throw"]),

    "Nosepass": Pokemon("Nosepass", "rock", 5, ["tackle", "rock-throw"], "Probopass", 40),

    "Probopass": Pokemon("Probopass", "rock", 1, ["tackle", "rock-throw"]),

    "Larvitar": Pokemon("Larvitar", "rock", 5, ["bite", "rock-throw"], "Pupitar", 30),

    "Pupitar": Pokemon("Pupitar", "rock", 1, ["bite", "rock-throw"], "Tyranitar", 55),

    "Tyranitar": Pokemon("Tyranitar", "rock", 1, ["bite", "rock-throw"]),

    # Ice type Pokémon
    "Snorunt": Pokemon("Snorunt", "ice", 5, ["scratch", "powder-snow"], "Glalie", 42),

    "Glalie": Pokemon("Glalie", "ice", 1, ["scratch", "powder-snow"]),
    
    "Swinub": Pokemon("Swinub", "ice", 5, ["tackle", "powder-snow"], "Piloswine", 33),

    "Piloswine": Pokemon("Piloswine", "ice", 1, ["tackle", "powder-snow"], "Mamoswine", 48),

    "Mamoswine": Pokemon("Mamoswine", "ice", 1, ["tackle", "powder-snow"]),
    
    "Snom": Pokemon("Snom", "ice", 5, ["tackle", "powder-snow"], "Frosmoth", 42),

    "Frosmoth": Pokemon("Frosmoth", "ice", 1, ["tackle", "powder-snow"]),
    
    "Vanillite": Pokemon("Vanillite", "ice", 5, ["icicle-spear", "powder-snow"], "Vanillish", 35),

    "Vanillish": Pokemon("Vanillish", "ice", 1, ["icicle-spear", "powder-snow"], "Vanilluxe", 47),

    "Vanilluxe": Pokemon("Vanilluxe", "ice", 1, ["icicle-spear", "powder-snow"]),
    
    "Cubchoo": Pokemon("Cubchoo", "ice", 5, ["growl", "powder-snow"], "Beartic", 37),

    "Beartic": Pokemon("Beartic", "ice", 1, ["growl", "powder-snow"]),
    
    "Spheal": Pokemon("Spheal", "ice", 5, ["powder-snow", "growl"], "Sealeo", 32),

    "Sealeo": Pokemon("Sealeo", "ice", 1, ["powder-snow", "growl"], "Walrein", 44),

    "Walrein": Pokemon("Walrein", "ice", 1, ["powder-snow", "growl"]),
    
    "Bergmite": Pokemon("Bergmite", "ice", 5, ["tackle", "powder-snow"], "Avalugg", 37),

    "Avalugg": Pokemon("Avalugg", "ice", 1, ["tackle", "powder-snow"]),
    
    "Sneasel": Pokemon("Sneasel", "ice", 5, ["scratch", "quick-attack"], "Weavile", 40),

    "Weavile": Pokemon("Weavile", "ice", 1, ["scratch", "quick-attack"]),
    
    "Delibird": Pokemon("Delibird", "ice", 5, ["present", "quick-attack"]),
    
    "Snover": Pokemon("Snover", "ice", 5, ["powder-snow", "leer"], "Abomasnow", 40),

    "Abomasnow": Pokemon("Abomasnow", "ice", 1, ["powder-snow", "leer"]),

    #Steel type Pokémon
    "Klink": Pokemon("Klink", "steel", 5, ["vice-grip", "thunder-shock"], "Klang", 38),

    "Klang": Pokemon("Klang", "steel", 1, ["vice-grip", "thunder-shock"], "Klinklang", 49),

    "Klinklang": Pokemon("Klinklang", "steel", 1, ["vice-grip", "thunder-shock"]),

    "Porygon": Pokemon("Porygon", "steel", 5, ["tackle", "conversion"], "Porygon2", 30),

    "Porygon2": Pokemon("Porygon2", "steel", 1, ["tackle", "conversion"], "Porygon-Z", 40),

    "Porygon-Z": Pokemon("Porygon-Z", "steel", 1, ["tackle", "conversion"]),
  
    "Aron": Pokemon("Aron", "steel", 5, ["tackle", "harden"], "Lairon", 32),

    "Lairon": Pokemon("Lairon", "steel", 1, ["tackle", "harden"], "Aggron", 42),

    "Aggron": Pokemon("Aggron", "steel", 1, ["tackle", "harden"]),
   
    "Beldum": Pokemon("Beldum", "steel", 5, ["take-down", "iron-defense"], "Metang", 20),

    "Metang": Pokemon("Metang", "steel", 1, ["take-down", "iron-defense"], "Metagross", 45),

    "Metagross": Pokemon("Metagross", "steel", 1, ["take-down", "iron-defense"]),
   
    "Pawniard": Pokemon("Pawniard", "steel", 5, ["scratch", "leer"], "Bisharp", 52),

    "Bisharp": Pokemon("Bisharp", "steel", 1, ["scratch", "leer"]),
    
    "Honedge": Pokemon("Honedge", "steel", 5, ["tackle", "swords-dance"], "Doublade", 35),

    "Doublade": Pokemon("Doublade", "steel", 1, ["tackle", "swords-dance"], "Aegislash", 45),

    "Aegislash": Pokemon("Aegislash", "steel", 1, ["tackle", "swords-dance"]),
    
    "Klefki": Pokemon("Klefki", "steel", 5, ["tackle", "fairy-lock"]),
    
    "Meltan": Pokemon("Meltan", "steel", 5, ["tackle", "harden"], "Melmetal", 30),

    "Melmetal": Pokemon("Melmetal", "steel", 1, ["tackle", "harden"]),

    #Bug type Pokémon
    "Caterpie": Pokemon("Caterpie", "bug", 5, ["tackle", "string-shot"], "Metapod", 7),

    "Metapod": Pokemon("Metapod", "bug", 1, ["tackle", "string-shot"], "Butterfree", 10),

    "Butterfree": Pokemon("Butterfree", "bug", 1, ["tackle", "string-shot"]),
    
    "Weedle": Pokemon("Weedle", "bug", 5, ["poison-sting", "string-shot"], "Kakuna", 7),

    "Kakuna": Pokemon("Kakuna", "bug", 1, ["poison-sting", "string-shot"], "Beedrill", 10),

    "Beedrill": Pokemon("Beedrill", "bug", 1, ["poison-sting", "string-shot"]),
    
    "Paras": Pokemon("Paras", "bug", 5, ["scratch", "stun-spore"], "Parasect", 24),

    "Parasect": Pokemon("Parasect", "bug", 1, ["scratch", "stun-spore"]),
    
    "Venonat": Pokemon("Venonat", "bug", 5, ["tackle", "confusion"], "Venomoth", 31),

    "Venomoth": Pokemon("Venomoth", "bug", 1, ["tackle", "confusion"]),
    
    "Pineco": Pokemon("Pineco", "bug", 5, ["tackle", "protect"], "Forretress", 31),

    "Forretress": Pokemon("Forretress", "bug", 1, ["tackle", "protect"]),
    
    "Shelmet": Pokemon("Shelmet", "bug", 5, ["acid", "bide"], "Accelgor", 30),

    "Accelgor": Pokemon("Accelgor", "bug", 1, ["acid", "bide"]),
    
    "Kricketot": Pokemon("Kricketot", "bug", 5, ["bide", "growl"], "Kricketune", 10),

    "Kricketune": Pokemon("Kricketune", "bug", 1, ["bide", "growl"]),
    
    "Burmy": Pokemon("Burmy", "bug", 5, ["protect", "tackle"], "Wormadam", 20),

    "Wormadam": Pokemon("Wormadam", "bug", 1, ["protect", "tackle"]),
    
    "Sewaddle": Pokemon("Sewaddle", "bug", 5, ["tackle", "string-shot"], "Swadloon", 20),

    "Swadloon": Pokemon("Swadloon", "bug", 1, ["tackle", "string-shot"], "Leavanny", 30),

    "Leavanny": Pokemon("Leavanny", "bug", 1, ["tackle", "string-shot"]),

    # Fighting type Pokémon
    "Hitmonlee": Pokemon("Hitmonlee", "fighting", 5, ["double-kick", "low-kick"]),
    
    "Hitmonchan": Pokemon("Hitmonchan", "fighting", 5, ["comet-punch", "agility"]),
    
    "Hitmontop": Pokemon("Hitmontop", "fighting", 5, ["tackle", "focus-energy"]),
    
    "Machop": Pokemon("Machop", "fighting", 5, ["low-kick", "leer"], "Machoke", 28),

    "Machoke": Pokemon("Machoke", "fighting", 1, ["low-kick", "leer"], "Machamp", 40),

    "Machamp": Pokemon("Machamp", "fighting", 1, ["low-kick", "leer"]),
    
    "Mankey": Pokemon("Mankey", "fighting", 5, ["scratch", "leer"], "Primeape", 28),

    "Primeape": Pokemon("Primeape", "fighting", 1, ["scratch", "leer"]),
    
    "Makuhita": Pokemon("Makuhita", "fighting", 5, ["tackle", "focus-energy"], "Hariyama", 24),

    "Hariyama": Pokemon("Hariyama", "fighting", 1, ["tackle", "focus-energy"]),
    
    "Riolu": Pokemon("Riolu", "fighting", 5, ["quick-attack", "foresight"], "Lucario", 30),

    "Lucario": Pokemon("Lucario", "fighting", 1, ["quick-attack", "foresight"]),
    
    "Throh": Pokemon("Throh", "fighting", 5, ["bind", "leer"]),
    
    "Sawk": Pokemon("Sawk", "fighting", 5, ["rock-smash", "leer"]),
    
    "Hawlucha": Pokemon("Hawlucha", "fighting", 5, ["tackle", "hone-claws"]),

    #Flying type Pokémon
    "Pidgey": Pokemon("Pidgey", "flying", 5, ["tackle", "gust"], "Pidgeotto", 18),

    "Pidgeotto": Pokemon("Pidgeotto", "flying", 1, ["tackle", "gust"], "Pidgeot", 36),

    "Pidgeot": Pokemon("Pidgeot", "flying", 1, ["tackle", "gust"]),
    
    "Spearow": Pokemon("Spearow", "flying", 5, ["peck", "growl"], "Fearow", 20),

    "Fearow": Pokemon("Fearow", "flying", 1, ["peck", "growl"]),
    
    "Farfetchd": Pokemon("Farfetchd", "normal", 5, ["peck", "sand-attack"], "Sirfetchd", 30),

    "Sirfetchd": Pokemon("Sirfetchd", "normal", 1, ["peck", "sand-attack"]),
    
    "Doduo": Pokemon("Doduo", "flying", 5, ["peck", "growl"], "Dodrio", 31),

    "Dodrio": Pokemon("Dodrio", "flying", 1, ["peck", "growl"]),
    
    "Hoothoot": Pokemon("Hoothoot", "flying", 5, ["tackle", "growl"], "Noctowl", 20),

    "Noctowl": Pokemon("Noctowl", "flying", 1, ["tackle", "growl"]),
    
    "Taillow": Pokemon("Taillow", "flying", 5, ["peck", "growl"], "Swellow", 22),

    "Swellow": Pokemon("Swellow", "flying", 1, ["peck", "growl"]),
    
    "Starly": Pokemon("Starly", "flying", 5, ["tackle", "growl"], "Staravia", 14),

    "Staravia": Pokemon("Staravia", "flying", 1, ["tackle", "growl"], "Staraptor", 34),

    "Staraptor": Pokemon("Staraptor", "flying", 1, ["tackle", "growl"]),
    
    "Pidove": Pokemon("Pidove", "flying", 5, ["gust", "growl"], "Tranquill", 21),

    "Tranquill": Pokemon("Tranquill", "flying", 1, ["gust", "growl"], "Unfezant", 32),

    "Unfezant": Pokemon("Unfezant", "flying", 1, ["gust", "growl"]),
    
    "Aerodactyl": Pokemon("Aerodactyl", "flying", 5, ["bite", "wing-attack"]),
    
    "Swablu": Pokemon("Swablu", "flying", 5, ["peck", "growl"], "Altaria", 35),

    "Altaria": Pokemon("Altaria", "flying", 1, ["peck", "growl"]),

    #Poison type Pokémon
    "Zubat": Pokemon("Zubat", "poison", 5, ["leech-life", "supersonic"], "Golbat", 22),

    "Golbat": Pokemon("Golbat", "poison", 1, ["leech-life", "supersonic"], "Crobat", 40),

    "Crobat": Pokemon("Crobat", "poison", 1, ["leech-life", "supersonic"]),

    "Grimer": Pokemon("Grimer", "poison", 5, ["scratch", "poison-gas"], "Muk", 38),

    "Muk": Pokemon("Muk", "poison", 1, ["scratch", "poison-gas"]),

    "Koffing": Pokemon("Koffing", "poison", 5, ["tackle", "smog"], "Weezing", 35),

    "Weezing": Pokemon("Weezing", "poison", 1, ["tackle", "smog"]),

    "Croagunk": Pokemon("Croagunk", "poison", 5, ["astonish", "mud-slap"], "Toxicroak", 37),

    "Toxicroak": Pokemon("Toxicroak", "poison", 1, ["astonish", "mud-slap"]),

    "Trubbish": Pokemon("Trubbish", "poison", 5, ["scratch", "poison-gas"], "Garbodor", 36),

    "Garbodor": Pokemon("Garbodor", "poison", 1, ["scratch", "poison-gas"]),

    "Venipede": Pokemon("Venipede", "poison", 5, ["poison-sting", "rollout"], "Whirlipede", 22),

    "Whirlipede": Pokemon("Whirlipede", "poison", 1, ["poison-sting", "rollout"], "Scolipede", 30),

    "Scolipede": Pokemon("Scolipede", "poison", 1, ["poison-sting", "rollout"]),

    "Skorupi": Pokemon("Skorupi", "poison", 5, ["bite", "poison-sting"], "Drapion", 40),

    "Drapion": Pokemon("Drapion", "poison", 1, ["bite", "poison-sting"]),

    "Stunky": Pokemon("Stunky", "poison", 5, ["scratch", "focus-energy"], "Skuntank", 34),

    "Skuntank": Pokemon("Skuntank", "poison", 1, ["scratch", "focus-energy"]),

    "Nidoran-f": Pokemon("Nidoran-f", "poison", 5, ["growl", "scratch"], "Nidorina", 16),

    "Nidorina": Pokemon("Nidorina", "poison", 1, ["growl", "scratch"], "Nidoqueen", 36),

    "Nidoqueen": Pokemon("Nidoqueen", "poison", 1, ["growl", "scratch"]),

    "Nidoran-m": Pokemon("Nidoran-m", "poison", 5, ["leer", "peck"], "Nidorino", 16),

    "Nidorino": Pokemon("Nidorino", "poison", 1, ["leer", "peck"], "Nidoking", 36),

    "Nidoking": Pokemon("Nidoking", "poison", 1, ["leer", "peck"]),

    #Ghost type Pokémon
    "Sandygast": Pokemon("Sandygast", "ghost", 5, ["astonish", "tackle"], "Palossand", 42),

    "Palossand": Pokemon("Palossand", "ghost", 1, ["astonish", "tackle"]),

    "Gastly": Pokemon("Gastly", "ghost", 5, ["lick", "hypnosis"], "Haunter", 25),

    "Haunter": Pokemon("Haunter", "ghost", 1, ["lick", "hypnosis"], "Gengar", 40),

    "Gengar": Pokemon("Gengar", "ghost", 1, ["lick", "hypnosis"]),
    
    "Shuppet": Pokemon("Shuppet", "ghost", 5, ["knock-off", "screech"], "Banette", 37),

    "Banette": Pokemon("Banette", "ghost", 1, ["knock-off", "screech"]),
    
    "Litwick": Pokemon("Litwick", "ghost", 5, ["ember", "astonish"], "Lampent", 41),

    "Lampent": Pokemon("Lampent", "ghost", 1, ["ember", "astonish"], "Chandelure", 50),

    "Chandelure": Pokemon("Chandelure", "ghost", 1, ["ember", "astonish"]),
    
    "Yamask": Pokemon("Yamask", "ghost", 5, ["astonish", "protect"], "Cofagrigus", 34),

    "Cofagrigus": Pokemon("Cofagrigus", "ghost", 1, ["astonish", "protect"]),
    
    "Phantump": Pokemon("Phantump", "ghost", 5, ["confuse-ray", "astonish"], "Trevenant", 41),

    "Trevenant": Pokemon("Trevenant", "ghost", 1, ["confuse-ray", "astonish"]),
    
    "Sableye": Pokemon("Sableye", "ghost", 5, ["leer", "scratch"]),
    
    "Drifloon": Pokemon("Drifloon", "ghost", 5, ["constrict", "minimize"], "Drifblim", 41),

    "Drifblim": Pokemon("Drifblim", "ghost", 1, ["constrict", "minimize"]),
    
    "Duskull": Pokemon("Duskull", "ghost", 5, ["night-shade", "leer"], "Dusclops", 37),

    "Dusclops": Pokemon("Dusclops", "ghost", 1, ["night-shade", "leer"], "Dusknoir", 47),

    "Dusknoir": Pokemon("Dusknoir", "ghost", 1, ["night-shade", "leer"]),
    
    "Spiritomb": Pokemon("Spiritomb", "ghost", 5, ["pursuit", "confuse-ray"]),
    
    "Misdreavus": Pokemon("Misdreavus", "ghost", 5, ["growl", "psywave"], "Mismagius", 30),

    "Mismagius": Pokemon("Mismagius", "ghost", 1, ["growl", "psywave"]),

    #Dragon type Pokémon
    "Dratini": Pokemon("Dratini", "dragon", 5, ["wrap", "leer"], "Dragonair", 30),

    "Dragonair": Pokemon("Dragonair", "dragon", 1, ["wrap", "leer"], "Dragonite", 55),

    "Dragonite": Pokemon("Dragonite", "dragon", 1, ["wrap", "leer"]),
    
    "Bagon": Pokemon("Bagon", "dragon", 5, ["rage", "bite"], "Shelgon", 30),

    "Shelgon": Pokemon("Shelgon", "dragon", 1, ["rage", "bite"], "Salamence", 50),

    "Salamence": Pokemon("Salamence", "dragon", 1, ["rage", "bite"]),
    
    "Axew": Pokemon("Axew", "dragon", 5, ["scratch", "dragon-rage"], "Fraxure", 38),

    "Fraxure": Pokemon("Fraxure", "dragon", 1, ["scratch", "dragon-rage"], "Haxorus", 48),

    "Haxorus": Pokemon("Haxorus", "dragon", 1, ["scratch", "dragon-rage"]),
    
    "Deino": Pokemon("Deino", "dragon", 5, ["tackle", "dragon-rage"], "Zweilous", 50),

    "Zweilous": Pokemon("Zweilous", "dragon", 1, ["tackle", "dragon-rage"], "Hydreigon", 64),

    "Hydreigon": Pokemon("Hydreigon", "dragon", 1, ["tackle", "dragon-rage"]),
    
    "Druddigon": Pokemon("Druddigon", "dragon", 5, ["leer", "scratch"])
}