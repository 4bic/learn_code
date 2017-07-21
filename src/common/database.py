import pymongo

class Database(object):
    """docstring for Database."""
    URI = " mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['4bic']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].find(query)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find_one(query)
