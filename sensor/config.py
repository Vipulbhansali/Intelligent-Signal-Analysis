import pymongo
import pandas as pd
import json
from dataclasses import dataclass
# Provide the mongodb localhost url to connect python to mongodb.
import os

@dataclass    #With the @dataclass decorator, Python automatically generates special methods like __init__(), __repr__(), __eq__(), and others 
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_access_secret_key:str = os.getenv("AWS_SECRET_ACCESS_KEY")





env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "class"