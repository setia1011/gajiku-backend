import datetime
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    username: str
    password: str
    email: str
    name: str
    group_id: Optional[int]
    client: Optional[int]
    id_type: Optional[int]
    id_number: Optional[int]
    phone: Optional[str]
    address: Optional[str]
    status: Optional[str]
    creator: int
    creator_at: datetime.datetime
    editor: Optional[int]
    updated_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class UserInfoOut(BaseModel):
    name: str
    email: str


class UpdateUser(BaseModel):
    email: Optional[str]
    name: Optional[str]
    id_type: Optional[int]
    id_number: Optional[int]
    phone: Optional[str]
    address: Optional[str]

    class Config:
        orm_mode = True


class UpdateGroup(BaseModel):
    group_id: int

    class Config:
        orm_mode = True


class CreateUser(BaseModel):
    name: str
    username: str
    password: str
    email: str

    class Config:
        orm_mode = True


class DeleteUser(BaseModel):
    id: int
    deleter: str


class UpdatePassword(BaseModel):
    old_password: str
    new_password: str
    confirm_new_password: str

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class CreateActivation(BaseModel):
    user_id: int
    acticode: str
    expired: datetime.datetime

    class Config:
        orm_mode = True


class Activation(BaseModel):
    acticode: str

    class Config:
        orm_mode = True


class UserByUsername(BaseModel):
    username: str

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


class ReadUserDetail(User):
    ref_group = UserGroup
    ref_id_type: Optional[UserIdType]

    class Config:
        orm_mode = True

