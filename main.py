# FastAPI reads paths liner my line, is value has same path it will be overriden with earlier one
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi import HTTPException


# to initialize: uvicorn main:app --reload

app = FastAPI()

db = [
    {
       "name": "bob", 
       "user_id": 1
    },
    {
       "name": "ally", 
       "user_id": 2
    },
    {
       "name": "matt", 
       "user_id": 3
    }
]
    


@app.get("/database")
# shows db
def read_root():
    return db
    
class User(BaseModel):
    name:str
    user_id: int

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
def get_user(id: int):
    count = 0
    sz = len(db)
    for acc in db:
        if id == acc["user_id"]:
            return acc
        count += 1
        if count == sz:
            raise HTTPException(status_code=409, detail = "Account not found") 
    

class AddText(BaseModel):
    text: str

@app.put("/user")
def put_text(user_id: int, text: AddText):
    for acc in db:
        if acc["user_id"] == user_id:
            acc["text"] = text.text
            return acc
    raise HTTPException(status_code=404, detail="User not found")
    


