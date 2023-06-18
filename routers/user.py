from fastapi import APIRouter, Path

from fastapi.responses import JSONResponse, Response

from fastapi.exceptions import HTTPException

from fastapi.encoders import jsonable_encoder

from models.user import User, users_db

from schemas.users import users_serializer, user_serializer

from typing import List

from config.db import collection

from bson import ObjectId

import uuid

user_router = APIRouter()

@user_router.get('/users', tags=['users'])
async def get_all_users():
    users = users_serializer(collection.find())
    return JSONResponse(content=jsonable_encoder(users), status_code=200)

@user_router.get('/users/{id}', tags=['users'])
async def get_user_by_id(id: str):
    user = users_serializer(collection.find({"_id": ObjectId(id)}))
    if user == []:
        raise HTTPException(status_code=404, detail="User not found")
    return JSONResponse(content=jsonable_encoder(user), status_code=200)

@user_router.post('/user', tags=['users'])
async def create_user(user: User):
    _id = collection.insert_one(dict(user))
    user = users_serializer(collection.find({"_id": _id.inserted_id}))
    return JSONResponse(content=jsonable_encoder({
        "message": "user registered succesfullly",
        "data": user
        }), status_code=201)

@user_router.put('/users/{id}', tags=['users'])
async def update_user_by_id(id: str, user: User):
    old_user = users_serializer(collection.find({"_id": ObjectId(id)}))
    if old_user == []:
        raise HTTPException(status_code=404, detail="User not found")
    
    collection.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })

    return JSONResponse(content=jsonable_encoder({
        "message": "user registered succesfullly",
        "data": user
        }), status_code=201)

@user_router.delete('/users/{id}', tags=['users'], status_code=204)
async def delete_user_by_id(id: str):
    old_user = users_serializer(collection.find({"_id": ObjectId(id)}))
    if old_user == []:
        raise HTTPException(status_code=404, detail="User not found")

    collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "user deleted successfully"}