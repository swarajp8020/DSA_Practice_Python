from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from threading import Lock

app = FastAPI()
users_db: Dict[int, dict]={}
lock = Lock()

class UserRequest(BaseModel):
    user_id: int
    name: str
@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="user not found")
    return users_db[user_id]
@app.post("/user")
def create_user(user: UserRequest):
    with lock:
        if user.user_id in users_db:
            raise HTTPException(status_code=400, detail="user already exists")
        users_db[user.user_id]={
            "user_id":user.user_id,
            "name":user.name
        }
    return users_db[user.user_id]