# A Base slack API

# Illustrate basic usage of FastAPI w/ MongoDB

from pymongo import MongoClient
from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List


DB = "DebProject"
DB_COLLECTION ="Test"

# Message defined in pydantic

class Message(BaseModel):
    channel: str
    athour: str
    text: str
    
# isinstiate the FastAPI

app = FastAPI()

# Get status
@app.get('/status')
def get_status():
    """Get status of messaging server."""
    return {"status": "running"}

@app.get("/channels", response_model=List[str])
def app_channel():
    """Get all channels in list from."""
    with MongoClient() as client:
        msg_collection = client[DB][DB_COLLECTION]
        distint_channel_list = msg_collection.distinct('channel')
        return distint_channel_list

@app.get("/messages/{channel}", response_model=List[Message])
def get_messages(channel: str):
    """Get all messages for the specified channel."""
    with MongoClient() as client:
        msg_collection = client[DB][DB_COLLECTION]
        msg_list = msg_collection.find({"channel": channel})
        response_msg_list = []
        for msg in msg_list:
            print(msg)
            response_msg_list.append(Message(**msg))
            return response_msg_list
            
            
@app.post("/post_message", status_code=status.HTTP_201_CREATED)
def post_message(message: Message):
    """Post a new message to the specified channel."""
    with MongoClient() as client:
        msg_collection = client[DB][DB_COLLECTION]
        
        result = msg_collection.insert_one(message.dict())
        ack = result.acknowledged
        return {"insert": "ok"}