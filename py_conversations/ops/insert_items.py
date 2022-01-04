from pymongo import MongoClient
from pymongo.errors import BulkWriteError, ConfigurationError
from dagster import op, In, Out, get_dagster_logger
from pymongo.results import InsertManyResult

import settings

MONGO_USERNAME = settings.MONGO_USERNAME
MONGO_PW = settings.MONGO_PW
MONGO_CLUSTER_NAME = settings.MONGO_CLUSTER_NAME
MONGO_DB_NAME = settings.MONGO_DB_NAME


@op(
    ins={
        'items': In(list)
    },
    out=Out(InsertManyResult)
)
def insert_items(items):
    logger = get_dagster_logger()
    try:
        client = MongoClient(
            f'mongodb+srv://{MONGO_USERNAME}:{MONGO_PW}@{MONGO_CLUSTER_NAME}.seck8.mongodb.net/?retryWrites=true&w=majority'
        )
        logger.info(client)
    except ConfigurationError as e:
        logger.error(e)

    db = client[MONGO_DB_NAME]
    collection = db['googlenews']

    try:
        result = collection.insert_many(items)
        return result
    except BulkWriteError as e:
        logger.error(e)
