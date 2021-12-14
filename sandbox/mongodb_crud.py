import logging

from pymongo import MongoClient
from pprint import pprint

from pymongo.errors import BulkWriteError

import settings

MONGO_USERNAME = settings.MONGO_USERNAME
MONGO_PW = settings.MONGO_PW
MONGO_CLUSTER_NAME = settings.MONGO_CLUSTER_NAME
MONGO_DB_NAME = settings.MONGO_DB_NAME

client = MongoClient(
    f'mongodb+srv://{MONGO_USERNAME}:{MONGO_PW}@{MONGO_CLUSTER_NAME}.seck8.mongodb.net/{MONGO_DB_NAME}?retryWrites=true&w=majority'
)

db_list = client.list_database_names()
pprint(db_list)

new_db = client['test_db']
new_coll = new_db['test_collection']

test_items = [
    {"item": "journal",
     "qty": 25,
     "tags": ["blank", "red"],
     "size": {"h": 14, "w": 21, "uom": "cm"}},
    {"item": "mat",
     "qty": 85,
     "tags": ["gray"],
     "size": {"h": 27.9, "w": 35.5, "uom": "cm"}},
    {"item": "mousepad",
     "qty": 25,
     "tags": ["gel", "blue"],
     "size": {"h": 19, "w": 22.85, "uom": "cm"}}]
try:
    result = new_coll.insert_many(test_items)
except BulkWriteError as e:
    logging.error(e)
print('Result acknowledged?: ', result.acknowledged)

coll_list = new_db.list_collection_names()
pprint(coll_list)
db = client['test_db']
print(db)
# serverStatusResult = db.command('serverStatus')
# pprint(serverStatusResult)
