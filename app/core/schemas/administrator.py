from pydantic import BaseModel
from typing import Optional


class ResponseOut(BaseModel):
    data: str


class ActivateSubscription(BaseModel):
    subs_id: int

    class Config:
        orm_mode = True
