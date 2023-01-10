from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def getName():
    return {"Name": "Emmy"}