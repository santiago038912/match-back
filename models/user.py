from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from typing import Optional

class User(BaseModel):
    # id: Optional[str] = None
    name: Optional[str] = Field()
    last_name: Optional[str] = Field()
    email: Optional[str] = Field()
    phone_number: Optional[str] = Field()
    password: Optional[str] = Field()

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