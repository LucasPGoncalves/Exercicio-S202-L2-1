from typing import Collection
import pymongo
from dataset.pokemon_dataset import dataset


class Database:
    def __init__(self, database, collection):
        connectionString = "mongodb+srv://Lucas:LpG1321321@cluster0.cnzoq.mongodb.net/Cluster0?retryWrites=true&w=majority"
        self.clusterConnection = pymongo.MongoClient(
            connectionString,
            tlsAllowInvalidCertificates=True # CASO OCORRA O ERRO [SSL_INVALID_CERTIFICATE]
        )
        self.db = self.clusterConnection[database]
        self.collection = self.db[collection]

    def resetDatabase(self):
        self.db.drop_collection(self.collection)
        self.collection.insert_many(dataset)

    def executeQuery(self, filters: dict):
        response = self.collection.find(filters)
        pokemons = []
        for pokemon in response:
            pokemons.append(pokemon)
        return pokemons

    def getFirePokemonsEvol(self):
        response = self.collection.find({"type": {"$all": ["Fire"]},"next_evolution":{"$exists": True}}, {
                                        "_id": 0, "name": 1, "type": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result

    def getFirePokemonsEvolSpawnRate(self):
        response = self.collection.find({"type": {"$all": ["Fire"]},"next_evolution":{"$exists": True},"spawn_chance":{"$gt":0.5}}, {
                                        "_id": 0, "name": 1, "type": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result

    def getEvolByName(self, name: str):
        response = self.collection.find({"name": name}, {
                                        "_id": 0, "next_evolution.0.name":1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result

    def getPokemonsHigherThan(self, height: str):
        response = self.collection.find({"height":height}, {
                                        "_id": 0, "name":1,"height":1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result 

    def getRarerPokemons(self):
        response = self.collection.find({"spawn_chance" : {"$lte":0.01}}, {
                                        "_id": 0, "name":1, "spawn_chance":1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result                         

