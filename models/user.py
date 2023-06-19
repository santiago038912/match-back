from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from typing import Optional

class User(BaseModel):
    name: str = Field()
    email: str = Field()
    phone_number: str = Field()
    password: str = Field()

    class Config():
        schema_extra = {
            "example": {
                "name": "default_name",
                "last_name": "default_lastname",
                "email": "default_email",
                "phone_number": "default_phone",
                "password": "default_password", 
            }
        }

class UserUpdate(BaseModel):
    name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    phone_number: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)