from fastapi import APIRouter, Path

from schemas.user import User, users_db

from typing import List

user_router = APIRouter()

@user_router.get('/users', tags=['users'])
def get_all_users() -> List[User]:
    return users_db

@user_router.get('/users/{name}', tags=['users'])
def get_user_by_name(name: str = Path()) -> List[User]:
    response = []
    for user in users_db:
        if user["name"] == name:
            response.append(user)
    return response