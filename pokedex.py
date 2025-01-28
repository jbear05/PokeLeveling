from entities import Pokemon



pokedex = {
    # Electric type Pokémon
    "Pikachu": Pokemon("Pikachu", "electric", 5, ["quick-attack", "thunder-shock"]),

    "Rotom": Pokemon("Rotom", "electric", 5, ["thunder-shock", "astonish"]),

    "Magnemite": Pokemon("Magnemite", "electric", 5, ["tackle", "thunder-shock"]),

    # Grass type Pokémon
    "Bulbasaur": Pokemon("Bulbasaur", "grass", 5, ["tackle", "vine-whip"]),

    "Oddish": Pokemon("Oddish", "grass", 5, ["absorb", "acid"]),

    "Bellsprout": Pokemon("Bellsprout", "grass", 5, ["vine-whip", "acid"]),

    "Chikorita": Pokemon("Chikorita", "grass", 5, ["tackle", "razor-leaf"]),

    "Treecko": Pokemon("Treecko", "grass", 5, ["scratch", "absorb"]),

    "Turtwig": Pokemon("Turtwig", "grass", 5, ["tackle", "absorb"]),

    "Shroomish": Pokemon("Shroomish", "grass", 5, ["absorb", "tackle"]),

    # Fire type Pokémon
    "Charmander": Pokemon("Charmander", "fire", 5, ["tackle", "ember"]),
    
    "Magby": Pokemon("Magby", "fire", 5, ["tackle", "ember"]),
    
    "Slugma": Pokemon("Slugma", "fire", 5, ["tackle", "ember"]),
    
    "Darumaka": Pokemon("Darumaka", "fire", 5, ["scratch", "ember"]),
    
    "Rolycoly": Pokemon("Rolycoly", "fire", 5, ["scratch", "ember"]),

    "Vulpix": Pokemon("Vulpix", "fire", 5, ["ember", "quick-attack"]),
    
    "Growlithe": Pokemon("Growlithe", "fire", 5, ["bite", "ember"]),
    
    "Houndour": Pokemon("Houndour", "fire", 5, ["ember", "leer"]),
    
    "Numel": Pokemon("Numel", "fire", 5, ["tackle", "growl"]),
    
    "Torkoal": Pokemon("Torkoal", "fire", 5, ["ember", "withdraw"]),

    # Water type Pokémon
    "Squirtle": Pokemon("Squirtle", "water", 5, ["tackle", "water-gun"]),
    
    "Psyduck": Pokemon("Psyduck", "water", 5, ["scratch", "water-gun"]),
    
    "Tentacool": Pokemon("Tentacool", "water", 5, ["scratch", "wrap"]),
    
    "Slowpoke": Pokemon("Slowpoke", "water", 5, ["confusion", "water-gun"]),
    
    "Krabby": Pokemon("Krabby", "water", 5, ["scratch", "water-gun"]),

    "Horsea": Pokemon("Horsea", "water", 5, ["bubble", "water-gun"]),

    "Totodile": Pokemon("Totodile", "water", 5, ["scratch", "water-gun"]),

    "Mudkip": Pokemon("Mudkip", "water", 5, ["tackle", "water-gun"]),

    "Piplup": Pokemon("Piplup", "water", 5, ["scratch", "bubble"]),

    # Normal type Pokémon
    "Eevee": Pokemon("Eevee", "normal", 5, ["tackle", "swift"]),
    
    "Jigglypuff": Pokemon("Jigglypuff", "normal", 5, ["tackle", "sing"]),
    
    "Meowth": Pokemon("Meowth", "normal", 5, ["scratch", "pay-day"]),

    "Slakoth": Pokemon("Slakoth", "normal", 5, ["scratch", "yawn"]),

    # Ground type Pokémon
    "Sandshrew": Pokemon("Sandshrew", "ground", 5, ["scratch", "mud-slap"]),
    
    "Diglett": Pokemon("Diglett", "ground", 5, ["dig", "tackle"]),
    
    "Sandile": Pokemon("Sandile", "ground", 5, ["mud-slap", "tackle"]),

    "Trapinch": Pokemon("Trapinch", "ground", 5, ["bite"]),

    "Gible": Pokemon("Gible", "ground", 5, ["tackle"]),

    # Rock type Pokémon
    "Geodude": Pokemon("Geodude", "rock", 5, ["tackle", "rock-throw"]),
    
    "Onix": Pokemon("Onix", "rock", 5, ["tackle", "rock-throw"]),

    "Roggenrola": Pokemon("Roggenrola", "rock", 5, ["tackle", "rock-throw"]),

    "Nosepass": Pokemon("Nosepass", "rock", 5, ["tackle", "rock-throw"]),

    "Larvitar": Pokemon("Larvitar", "rock", 5, ["bite", "rock-throw"]),

    # Ice type Pokémon
    "Snorunt": Pokemon("Snorunt", "ice", 5, ["scratch", "powder-snow"]),
    
    "Swinub": Pokemon("Swinub", "ice", 5, ["tackle", "powder-snow"]),
    
    "Snom": Pokemon("Snom", "ice", 5, ["tackle", "powder-snow"]),
    
    "Vanillite": Pokemon("Vanillite", "ice", 5, ["icicle-spear", "powder-snow"]),
    
    "Cubchoo": Pokemon("Cubchoo", "ice", 5, ["growl", "powder-snow"]),
    
    "Spheal": Pokemon("Spheal", "ice", 5, ["powder-snow", "growl"]),
    
    "Bergmite": Pokemon("Bergmite", "ice", 5, ["tackle", "powder-snow"]),
    
    "Sneasel": Pokemon("Sneasel", "ice", 5, ["scratch", "quick-attack"]),
    
    "Delibird": Pokemon("Delibird", "ice", 5, ["present", "quick-attack"]),
    
    "Snover": Pokemon("Snover", "ice", 5, ["powder-snow", "leer"]),

    #Steel type Pokémon
    "Klink": Pokemon("Klink", "steel", 5, ["vice-grip", "thunder-shock"]),

    "Porygon": Pokemon("Porygon", "steel", 5, ["tackle", "conversion"]),
  
    "Aron": Pokemon("Aron", "steel", 5, ["tackle", "harden"]),
   
    "Beldum": Pokemon("Beldum", "steel", 5, ["take-down", "iron-defense"]),
   
    "Pawniard": Pokemon("Pawniard", "steel", 5, ["scratch", "leer"]),
    
    "Honedge": Pokemon("Honedge", "steel", 5, ["tackle", "swords-dance"]),
    
    "Klefki": Pokemon("Klefki", "steel", 5, ["tackle", "fairy-lock"]),
    
    "Meltan": Pokemon("Meltan", "steel", 5, ["tackle", "harden"]),

    #Bug type Pokémon
    "Caterpie": Pokemon("Caterpie", "bug", 5, ["tackle", "string-shot"]),
    
    "Weedle": Pokemon("Weedle", "bug", 5, ["poison-sting", "string-shot"]),
    
    "Paras": Pokemon("Paras", "bug", 5, ["scratch", "stun-spore"]),
    
    "Venonat": Pokemon("Venonat", "bug", 5, ["tackle", "confusion"]),
    
    "Pineco": Pokemon("Pineco", "bug", 5, ["tackle", "protect"]),
    
    "Shelmet": Pokemon("Shelmet", "bug", 5, ["acid", "bide"]),
    
    "Kricketot": Pokemon("Kricketot", "bug", 5, ["bide", "growl"]),
    
    "Burmy": Pokemon("Burmy", "bug", 5, ["protect", "tackle"]),
    
    "Sewaddle": Pokemon("Sewaddle", "bug", 5, ["tackle", "string-shot"]),

    # Fighting type Pokémon
    "Hitmonlee": Pokemon("Hitmonlee", "fighting", 5, ["double-kick", "low-kick"]),
    
    "Hitmonchan": Pokemon("Hitmonchan", "fighting", 5, ["comet-punch", "agility"]),
    
    "Hitmontop": Pokemon("Hitmontop", "fighting", 5, ["tackle", "focus-energy"]),
    
    "Machop": Pokemon("Machop", "fighting", 5, ["low-kick", "leer"]),
    
    "Mankey": Pokemon("Mankey", "fighting", 5, ["scratch", "leer"]),
    
    "Makuhita": Pokemon("Makuhita", "fighting", 5, ["tackle", "focus-energy"]),
    
    "Riolu": Pokemon("Riolu", "fighting", 5, ["quick-attack", "foresight"]),
    
    "Throh": Pokemon("Throh", "fighting", 5, ["bind", "leer"]),
    
    "Sawk": Pokemon("Sawk", "fighting", 5, ["rock-smash", "leer"]),
    
    "Hawlucha": Pokemon("Hawlucha", "fighting", 5, ["tackle", "hone-claws"]),

    #Flying type Pokémon
    "Pidgey": Pokemon("Pidgey", "flying", 5, ["tackle", "gust"]),
    
    "Spearow": Pokemon("Spearow", "flying", 5, ["peck", "growl"]),
    
    "Farfetchd": Pokemon("Farfetchd", "normal", 5, ["peck", "sand-attack"]),
    
    "Doduo": Pokemon("Doduo", "flying", 5, ["peck", "growl"]),
    
    "Hoothoot": Pokemon("Hoothoot", "flying", 5, ["tackle", "growl"]),
    
    "Taillow": Pokemon("Taillow", "flying", 5, ["peck", "growl"]),
    
    "Starly": Pokemon("Starly", "flying", 5, ["tackle", "growl"]),
    
    "Pidove": Pokemon("Pidove", "flying", 5, ["gust", "growl"]),
    
    "Aerodactyl": Pokemon("Aerodactyl", "flying", 5, ["bite", "wing-attack"]),
    
    "Swablu": Pokemon("Swablu", "flying", 5, ["peck", "growl"]),

    #Poison type Pokémon
    "Zubat": Pokemon("Zubat", "poison", 5, ["leech-life", "supersonic"]),

    "Grimer": Pokemon("Grimer", "poison", 5, ["scratch", "poison-gas"]),

    "Koffing": Pokemon("Koffing", "poison", 5, ["tackle", "smog"]),

    "Croagunk": Pokemon("Croagunk", "poison", 5, ["astonish", "mud-slap"]),

    "Trubbish": Pokemon("Trubbish", "poison", 5, ["scratch", "poison-gas"]),

    "Venipede": Pokemon("Venipede", "poison", 5, ["poison-sting", "rollout"]),

    "Skorupi": Pokemon("Skorupi", "poison", 5, ["bite", "poison-sting"]),

    "Stunky": Pokemon("Stunky", "poison", 5, ["scratch", "focus-energy"]),

    "Nidoran_f": Pokemon("Nidoran_f", "poison", 5, ["growl", "scratch"]),

    "Nidoran_m": Pokemon("Nidoran_m", "poison", 5, ["leer", "peck"]),

    #Ghost type Pokémon
    "Sandygast": Pokemon("Sandygast", "ghost", 5, ["astonish", "tackle"]),

    "Gastly": Pokemon("Gastly", "ghost", 5, ["lick", "hypnosis"]),
    
    "Shuppet": Pokemon("Shuppet", "ghost", 5, ["knock-off", "screech"]),
    
    "Litwick": Pokemon("Litwick", "ghost", 5, ["ember", "astonish"]),
    
    "Yamask": Pokemon("Yamask", "ghost", 5, ["astonish", "protect"]),
    
    "Phantump": Pokemon("Phantump", "ghost", 5, ["confuse-ray", "astonish"]),
    
    "Sableye": Pokemon("Sableye", "ghost", 5, ["leer", "scratch"]),
    
    "Drifloon": Pokemon("Drifloon", "ghost", 5, ["constrict", "minimize"]),
    
    "Duskull": Pokemon("Duskull", "ghost", 5, ["night-shade", "leer"]),
    
    "Spiritomb": Pokemon("Spiritomb", "ghost", 5, ["pursuit", "confuse-ray"]),
    
    "Misdreavus": Pokemon("Misdreavus", "ghost", 5, ["growl", "psywave"]),

    #Dragon type Pokémon
    "Dratini": Pokemon("Dratini", "dragon", 5, ["wrap", "leer"]),
    
    "Bagon": Pokemon("Bagon", "dragon", 5, ["rage", "bite"]),
    
    "Axew": Pokemon("Axew", "dragon", 5, ["scratch", "dragon-rage"]),
    
    "Deino": Pokemon("Deino", "dragon", 5, ["tackle", "dragon-rage"]),
    
    "Druddigon": Pokemon("Druddigon", "dragon", 5, ["leer", "scratch"])
}