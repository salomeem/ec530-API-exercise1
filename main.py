# FastAPI reads paths liner my line, is value has same path it will be overriden with earlier one
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi import HTTPException


# to initialize: uvicorn main:app --reload

app = FastAPI()

db = []

@app.get("/database")
# shows db
def read_root():
    return db
    
class User(BaseModel):
    name:str
    user_id: str

@app.post("/user")
# function to add user to db
def create_user(user:User):
    # use dot notation to access base model;
    for acc in db:
        print(user)
        if user.name == acc["name"]:
            raise HTTPException(status_code=409, detail = "Username already exists")
    user_info = {"name": user.name, "user_id": user.user_id}
    db.append(user_info)
    return db
    
@app.get("/user/{id}")
# function to get userid from db
def get_user(id):
    count = 0
    sz = len(db)
    for acc in db:
        if id == acc["user_id"]:
            return acc
        count += 1
        if count == sz:
            raise HTTPException(status_code=409, detail = "Account not found") 
    


