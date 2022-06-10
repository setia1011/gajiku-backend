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
    token: Optional[str]
    project_id: Optional[int]
    creator: Optional[int]
    created_at: Optional[datetime.datetime]
    editor: Optional[int]
    edited_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class SubscribePlan(BaseModel):
    subs_plan_id: int
    subs_month: int
    project_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "subs_plan_id": 2,
                "subs_month": 3,
                "project_id": 1
            }
        }


class SubscribeOut(BaseModel):
    id: Optional[int]
    plan: Optional[str]
    monthly_price: Optional[float]
    status: Optional[str]
    creator: Optional[int]
    created_at: Optional[datetime.datetime]
    editor: Optional[int]
    updated_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class User(BaseModel):
    name: Optional[str]


class SubscriptionPlan(BaseModel):
    plan: Optional[str]
    monthy_price: Optional[float]


# class SubscribePlanOut(User):




