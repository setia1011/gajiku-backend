import datetime

from pydantic import BaseModel
from typing import Optional


class Client(BaseModel):
    id: Optional[int]
    name: Optional[str]
    address: Optional[str]
    responsible_name: Optional[str]
    responsible_id_type: Optional[int]
    responsible_id_number: Optional[str]
    user_id: Optional[int]
    creator: Optional[int]
    created_at: Optional[datetime.datetime]
    editor: Optional[int]
    updated_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True