from pymongo import MongoClient
from config import Config


class Connect(object):
    @staticmethod
    def get_connection():
        if Config.TESTING:
            return MongoClient(Config.DB_SERVER).Development
        else:
            return MongoClient(Config.DB_SERVER).Production
