import datetime

from pydantic import BaseModel
from typing import Optional


class RefGroup(BaseModel):
    id: Optional[int]
    group_name: Optional[str]
    group_description: Optional[str]

    class Config:
        orm_mode = True


class RefIdType(BaseModel):
    id: Optional[int]
    id_type: Optional[str]
    id_description: Optional[str]

    class Config:
        orm_mode = True


class Group(BaseModel):
    group_name: str
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


class UserIdTypeIn(BaseModel):
    s: str

    class Config:
        orm_mode = True



class CreateUser(BaseModel):
    name: str
    username: str
    password: str
    email: str
    group_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Setiadi",
                "username": "setia",
                "password": "123",
                "email": "edu.setiadi.my@gmail.com",
                "group_id": 1
            }
        }