from typing import Optional
from fastapi import FastAPI
from pymongo import MongoClient
import pprint 

client = MongoClient()

db = client["DebProject"]
db_collection = db["Test"]

# Create a message dict
message = {
    "channel": "dev",
    "author": "cerami",
    "text": "Hello, world!"
    
}

result = db_collection.insert_one(message)
print(result.inserted_id)

# Retrieve DebProject Database collection

pp = pprint.PrettyPrinter(indent=4)
for doc in db_collection.find():
    pp.pprint(doc)

app = FastAPI()

@app.get("/")
def getName():
    return {"Name": "Emmy"}