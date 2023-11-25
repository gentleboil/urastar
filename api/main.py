from fastapi import FastAPI

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Brave new World"}

@app.get("/stritem/{stritem}")
async def stritem(stritem:ModelName):
    return {"stritem": stritem}

@app.get("/intitem/{intitem}")
async def intitem(intitem:int):
    return {"intitem": intitem}

