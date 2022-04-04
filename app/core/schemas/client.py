from pydantic import BaseModel
from typing import Optional


class Gaji(BaseModel):
    username: str
    group_description: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "group_name": "superuser",
                "group_description": "grandted all privileges"
            }
        }


class UserIdType(BaseModel):
    id_type: str
    id_description: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id_type": "nik",
                "id_description": "nomor induk kependudukan di indonesia"
            }
        }


class CreateUser(BaseModel):
    name: str
    username: str
    password: str
    email: str
    group: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Setiadi",
                "username": "setia",
                "password": "123",
                "email": "edu.setiadi.my@gmail.com",
                "group": 1
            }
        }