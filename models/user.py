from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from typing import Optional

class User(BaseModel):
    username: str
    name: str = Field()
    email: str = Field()
    phone_number: str = Field()
    password: str = Field()

    class Config():
        schema_extra = {
            "example": {
                "username": "default_username",
                "name": "default_name",
                "email": "default_email",
                "phone_number": "default_phone",
                "password": "default_password", 
            }
        }

class UserUpdate(BaseModel):
    username: str= Field(default=None)
    name: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    phone_number: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)

class UserDTO():
    username: str
    name: str
    email: str
    phone_number: str
    
