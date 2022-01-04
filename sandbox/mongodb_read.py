import logging

from pymongo import MongoClient
from pymongo.errors import ConfigurationError

import settings

MONGO_USERNAME = settings.MONGO_USERNAME
MONGO_PW = settings.MONGO_PW
MONGO_CLUSTER_NAME = settings.MONGO_CLUSTER_NAME
MONGO_DB_NAME = settings.MONGO_DB_NAME


if __name__ == '__main__':
    try:
        client = MongoClient(
            f'mongodb+srv://{MONGO_USERNAME}:{MONGO_PW}@{MONGO_CLUSTER_NAME}.seck8.mongodb.net/{MONGO_DB_NAME}?retryWrites=true&w=majority'
        )
    except ConfigurationError as e:
        logging.error(e)

    db_list = client.list_database_names()
    print(db_list)
    db = client.conversations
    collection = db['googlenews']
    filter = {
        'time': {
            '$gte': {
                '$date': '2022-01-01'}}}
    for doc in collection.find():
        print(doc)
