from mongoengine import connect
from pymongo import MongoClient

from models.ninjaModel import Ninja

TEST_DATABASE="app-test-db"
DEV_DATABASE="app-dev-db"
HOST="mongodb://localhost:27017"

# You can connect to a real mongo server instance by your own.

def init_connection(database,host):
    return connect(database, host=host, alias='default')


def init_db():

    n1 = Ninja(name='Akira')
    n1.save()

    n2 = Ninja(name='Teckshuo')
    n2.save()

def remove_db(database,host):
    client = MongoClient(host)
    client.drop_database(database)
