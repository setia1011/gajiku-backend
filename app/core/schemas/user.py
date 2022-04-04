import datetime
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
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
    # password: Optional[str]

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class UserRegister(BaseModel):
    name: str
    username: str
    password: str
    email: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    email: Optional[str]
    name: Optional[str]
    id_type: Optional[int]
    id_number: Optional[int]
    phone: Optional[str]
    address: Optional[str]

    class Config:
        orm_mode = True


class GroupUpdate(BaseModel):
    group_id: int

    class Config:
        orm_mode = True


class UpdatePassword(BaseModel):
    old_password: str
    new_password: str
    confirm_new_password: str

    class Config:
        orm_mode = True


class Activation(BaseModel):
    acticode: str

    class Config:
        orm_mode = True


class FindUserByUsername(BaseModel):
    username: str

    class Config:
        orm_mode = True


class UserGroup(BaseModel):
    id: Optional[str]
    group_description: Optional[str]
    group_name: Optional[str]

    class Config:
        orm_mode = True


class UserIdType(BaseModel):
    id: Optional[int]
    id_type: Optional[str]
    id_description: Optional[str]

    class Config:
        orm_mode = True


class UserClient(BaseModel):
    id: Optional[int]
    token: Optional[str]
    name: Optional[str]
    address: Optional[str]
    responsible: Optional[str]
    responsible_id_type: Optional[int]
    responsible_id_number: Optional[int]
    subscription_id: Optional[int]
    creator: Optional[int]
    created_at: Optional[datetime.datetime]
    editor: Optional[int]
    updated_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class ReadUserDetail(User):
    ref_group: UserGroup
    ref_id_type: Optional[UserIdType]
    ref_client: Optional[UserClient]

    class Config:
        orm_mode = True
