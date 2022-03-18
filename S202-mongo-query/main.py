from db.database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
# db.resetDatabase()

#pokemons = db.getFirePokemonsEvol()
#pokemons = db.getFirePokemonsEvolSpawnRate()
#pokemons = db.getPokemonEvolutionsByName("Bulbasaur")
#pokemons = db.getPokemonsHigherThan("2.01 m")
pokemons = db.getRarerPokemons()

writeAJson(pokemons,"pokemons")
