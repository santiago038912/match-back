from fastapi import APIRouter, Depends, HTTPException, status

from typing import Annotated

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from models.user import User

from utils.auth import get_current_user, fake_decode_token, fake_hash_password, UserInDB

from config.db import collection

from bson import ObjectId

auth_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@auth_router.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

@auth_router.get("/usersa/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user

@auth_router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    # user_dict = fake_users_db.get(form_data.username)
    user_dict = dict(collection.find_one({"_id": ObjectId(id)}))
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}