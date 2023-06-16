from pydantic import BaseModel, Field
from typing import Optional

users_db = [
    {
        "id": "w765r4erfghgre",
        "name": "Pedro",
        "last_name": "Picapiedra",
        "email": "pedro@gmail.com",
        "phone_number": "2343565",
        "password": "peofeo",
    },
    {
        "id": "5678iyhgb4-4tgfevc-3fed",
        "name": "Pedro",
        "last_name": "Cualquiera",
        "email": "pedro2@gmail.com",
        "phone_number": "2343565",
        "password": "peofeo",
    }
]

class User(BaseModel):
    id: Optional[str] = None
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