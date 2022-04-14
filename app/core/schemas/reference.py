import datetime

from pydantic import BaseModel
from typing import Optional


class RefUserGroup(BaseModel):
    id: Optional[int]
    group_name: Optional[str]
    group_description: Optional[str]

    class Config:
        orm_mode = True
