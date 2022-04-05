import datetime
from pydantic import BaseModel
from typing import Optional


class Subscription(BaseModel):
    id: Optional[int]
    subs_plan_id: Optional[int]
    subs_month: Optional[int]
    subs_price: Optional[float]
    subs_start: Optional[datetime.datetime]
    subs_end: Optional[datetime.datetime]
    creator: Optional[int]
    created_at: Optional[datetime.datetime]
    editor: Optional[int]
    edited_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class SubscribePlan(BaseModel):
    subs_plan_id: int
    subs_month: int
    subs_start: datetime.datetime
    creator: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "subs_plan_id": 2,
                "subs_month": 3,
                "subs_start": "2019-08-24T14:15:22Z",
                "creator": 1
            }
        }


class User(BaseModel):
    name: Optional[str]


class SubscriptionPlan(BaseModel):
    plan: Optional[str]
    monthy_price: Optional[float]


# class SubscribePlanOut(User):




