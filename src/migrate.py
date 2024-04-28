import os
import pandas as pd

from pymongo import MongoClient

client = MongoClient("mongodb://painel_esus-mongo:27017/esus")
collection = client.get_database()['atendimentos']

if collection.count_documents({}) == 0:
    df = pd.read_csv('./atendimentos.csv')
    data = df.to_dict(orient='records')
    collection.insert_many(data)