import os
import pandas as pd

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

client = MongoClient(os.getenv("MONGO_URI"))
collection = client.get_database()['atendimentos']

if collection.count_documents({}) == 0:
    df = pd.read_csv('./atendimentos.csv')
    data = df.to_dict(orient='records')
    collection.insert_many(data)