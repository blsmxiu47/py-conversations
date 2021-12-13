from pymongo import MongoClient
from pprint import pprint

MONGO_USERNAME = settings.MONGO_USERNAME
MONGO_PW = settings.MONGO_PW
MONGO_CLUSTER_NAME = settings.MONGO
MONGO_DB_NAME = settings.MONGO_DB_NAME

client = MongoClient(
    f'mongodb+srv://{MONGO_USERNAME}:{MONGO_PW}@{MONGO_CLUSTER_NAME}.seck8.mongodb.net/{MONGO_DB_NAME}?retryWrites=true&w=majority'
)
db = client.admin
serverStatusResult = db.command("serverStatus")
pprint(serverStatusResult)
