import datetime

from pydantic import BaseModel
from typing import Optional


class RefUserGroup(BaseModel):
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
