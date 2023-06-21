from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from config.db import collection

from middleware.error_handler import ErrorHandler

from typing import Annotated

from routers.user import user_router

from models.user import User

# APP_INFO
app = FastAPI()
app.title = "Match"
app.version = "0.0.1"

# MIDDLEWARE
# app.add_middleware(ErrorHandler)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# ROUTERS
app.include_router(user_router)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user