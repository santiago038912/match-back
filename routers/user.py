from fastapi import APIRouter, Path

from fastapi.responses import JSONResponse

from fastapi.exceptions import HTTPException

from fastapi.encoders import jsonable_encoder

from schemas.user import User, users_db

from typing import List

import uuid

user_router = APIRouter()

@user_router.get('/users', tags=['users'])
def get_all_users():
    return JSONResponse(content=jsonable_encoder(users_db), status_code=200)

@user_router.get('/users/{id}', tags=['users'])
def get_user_by_id(id: str = Path()):
    response = []
    for user in users_db:
        if user['id'] == id:
            response.append(user)
    if response:
        return JSONResponse(content=jsonable_encoder(response), status_code=200)
    else:
        raise HTTPException(status_code=404, detail="User not found")

@user_router.get('/users/{name}', tags=['users'])
def get_user_by_name(name: str = Path()):
    response = []
    for user in users_db:
        if user['name'] == name:
            response.append(user)
    if response:
        return JSONResponse(content=jsonable_encoder(response), status_code=200)
    else:
        raise HTTPException(status_code=404, detail="User not found")

@user_router.post('/users', tags=['users'])
def create_user(user: User):
    user.id = str(uuid.uuid4())
    users_db.append(user.dict())
    return JSONResponse(content=jsonable_encoder({"message":"user created successfully"}), status_code=201)

@user_router.put('/users/{id}', tags=['users'])
def update_user_by_id(id: str, new_user: User):
    for user in users_db:
        if user["id"] == id:
            user['name'] = new_user.name if new_user.name else user['name']
            user['last_name'] = new_user.last_name if new_user.last_name else user['last_name']
            user['email'] = new_user.email if new_user.email else user['email']
            user['phone_number'] = new_user.phone_number if new_user.phone_number else user['phone_number']
            user['password'] = new_user.password if new_user.password else user['password']

            return JSONResponse(content=jsonable_encoder({"message":"user updated successfully"}), status_code=201)
        
    raise HTTPException(status_code=404, detail="User not found")
        
@user_router.delete('/users/{id}', tags=['users'])
def delete_user_by_id(id: str):
    for user in users_db:
        if user["id"] == id:
            users_db.remove(user)
            return JSONResponse(content=jsonable_encoder({"message": "User deleted successfully"}), status_code=200)

    raise HTTPException(status_code=404, detail="User not found")