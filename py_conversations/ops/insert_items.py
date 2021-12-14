import logging

from pymongo import MongoClient
from pymongo.errors import BulkWriteError
from dagster import op

import settings

MONGO_USERNAME = settings.MONGO_USERNAME
MONGO_PW = settings.MONGO_PW
MONGO_CLUSTER_NAME = settings.MONGO_CLUSTER_NAME
MONGO_DB_NAME = settings.MONGO_DB_NAME


@op
def insert_items(collection_name, items):
    client = MongoClient(
        f'mongodb+srv://{MONGO_USERNAME}:{MONGO_PW}@{MONGO_CLUSTER_NAME}.seck8.mongodb.net/?retryWrites=true&w=majority'
    )

    db = client[MONGO_DB_NAME]
    collection = db[collection_name]

    try:
        result = collection.insert_many(items)
        return result
    except BulkWriteError as e:
        logging.error(e)
