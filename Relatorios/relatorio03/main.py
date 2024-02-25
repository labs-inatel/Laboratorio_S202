from database import Database
from save_json import writeAJson

db = Database(database="dex", collection="pokemons")
db.resetDatabase()
pokemons = db.collection.find()


# Search all Pokémon:
def viewPokemon():
    writeAJson(pokemons, "all_pokemon")


# Search Pokémon by dex number:
def getPokemonByDex(number: int):
    return db.collection.find({"id": number})


def inf_pokemons():
    cont = 0
    quant_pokemons = int(input("Enter the amount of pokemons:"))
    var_id = 1

    while cont < quant_pokemons:
        pokemon_arq = getPokemonByDex(var_id)
        text_id = str(var_id)
        writeAJson(pokemon_arq, "pokemon" + text_id)
        var_id = int(text_id) + 1
        cont += 1

pass

# Search Pokémon by types:
def getPokemonTypes():
    types_pokemons = input("Enter the types of pokemons:")
    pokemon = db.collection.find({"type": types_pokemons})
    writeAJson(pokemon, "pokemon_" + types_pokemons)


# Search Pokémon by HP:
def getPokemonHP():
    HP_pokemon = int(input("Enter the amount of pokemon's HP:"))
    pokemon = db.collection.find({"base.HP": {"$lte": HP_pokemon}})
    text_HP = str(HP_pokemon)
    writeAJson(pokemon, "pokemon_" + text_HP)


# Search Pokémon's names according to the amount of letters:
def getNamesPokemons(collection):
    letter_pokemon = int(input("Enter the amount of letters to find the pokemon's names:"))
    names = collection.find({}, {"name": 1})
    quant_letters = []

    for name in names:
        if len(name["name"].keys()) <= letter_pokemon:
            if all(len(word) <= letter_pokemon for word in name["name"].values()):
                quant_letters.append(name["name"].values())

    return quant_letters


# Calling the functions:

# viewPokemon()
# inf_pokemons()
# getPokemonTypes()
# getPokemonHP()
# writeAJson(getNamesPokemons(db.collection), "pokemon_names")
