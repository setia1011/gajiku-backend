import datetime

from pydantic import BaseModel
from typing import Optional, List


class UserBase(BaseModel):
    email: Optional[str]
    address: Optional[str]
    name: Optional[str]
    status: Optional[str]
    group_id: Optional[int]
    creator: Optional[int]
    client_id: Optional[int]
    created_at: Optional[datetime.datetime]
    id_type: Optional[int]
    editor: Optional[int]
    username: Optional[str]
    id_number: Optional[str]
    updated_at: Optional[datetime.datetime]
    id: Optional[int]
    phone: Optional[str]

    class Config:
        orm_mode = True


class UserLogin(UserBase):
    username: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "setia",
                "password": "123"
            }
        }


class UserOut(UserBase):
    data = UserBase

    class Config:
        orm_mode = True


class UserGroup(BaseModel):
    group_description: Optional[str]
    group_name: Optional[str]
    id: Optional[str]

    class Config:
        orm_mode = True


class UserIdType(BaseModel):
    id: Optional[int]
    id_type: Optional[str]
    id_description: Optional[str]

    class Config:
        orm_mode = True


class UserIn2(BaseModel):
    username: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "setia"
            }
        }


class ReadUserWithGroup(UserBase):
    ref_group: UserGroup
    ref_id_type: Optional[UserIdType]

    class Config:
        orm_mode = True
