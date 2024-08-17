import os
import sys
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
import pandas as pd
from network_security.exception.exception import NetworkSecurityException
from network_security.logger.logger import logging

# MongoDB URI directly from test.py
MONGO_DB_URL = "mongodb+srv://suhas:suhaspk990@cluster0.hqa5r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Print the MongoDB URL to verify
print(f"Using MongoDB URL: {MONGO_DB_URL}")

ca = certifi.where()

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def pushing_data_to_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            # Connect to MongoDB
            self.mongo_client = MongoClient(MONGO_DB_URL, server_api=ServerApi('1'))

            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]

            # Insert the records into the MongoDB collection
            self.collection.insert_many(self.records)

            return len(self.records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == '__main__':
    FILE_PATH = "./network_data/network_data.csv"
    DATABASE = "suhapk"
    COLLECTION = "NetworkData"
    networobj = NetworkDataExtract()
    records = networobj.csv_to_json_convertor(FILE_PATH)
    noofrecords = networobj.pushing_data_to_mongodb(records, DATABASE, COLLECTION)
    print(f"Number of records inserted: {noofrecords}")
