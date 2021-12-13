import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")

MONGO_USERNAME = os.environ.get("MONGO_USERNAME")
MONGO_PW = os.environ.get("MONGO_PW")
MONGO_CLUSTER_NAME = os.environ.get("MONGO_CLUSTER_NAME")
MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME")
