from typing import Annotated

from fastapi import Depends

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class UserInDB(User):
    hashed_password: str

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user

def fake_hash_password(password: str):
    return "fakehashed" + password
