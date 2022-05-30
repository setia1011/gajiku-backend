import datetime

from pydantic import BaseModel
from typing import Optional, List, Union


class UserIdType(BaseModel):
    id: Optional[int]
    id_type: Optional[str]
    id_description: Optional[str]

    class Config:
        orm_mode = True


class SubscriptionPlan(BaseModel):
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


class Subscription(BaseModel):
    id: Optional[int]
    subs_plan_id: Optional[int]
    subs_month: Optional[int]
    subs_price: Optional[float]
    subs_start: Optional[datetime.datetime]
    subs_end: Optional[datetime.datetime]
    token: Optional[str]
    project_id: Optional[int]
    status: Optional[str]
    creator: Optional[int]
    created_at: Optional[datetime.datetime]
    editor: Optional[int]
    updated_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class Project(BaseModel):
    id: Optional[int]
    project: Optional[str]
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


class ProjectDetail(BaseModel):
    project_id: int

    class Config:
        orm_mode = True


class ProjectDetailsOut(Project):
    ref_id_type: Optional[UserIdType]
    ref_subscription: Optional[list[Subscription]]

    class Config:
        orm_mode = True


class Subscription2(Subscription):
    ref_subscription_plan: Optional[SubscriptionPlan]


class ProjectDetailsOutV2(Project):
    ref_id_type: Optional[UserIdType]
    ref_subscription: Optional[list[Subscription2]]

    class Config:
        orm_mode = True


class SubscriptionDetailsOut(Subscription):
    ref_project: Optional[Project]
    ref_subscription_plan: Optional[SubscriptionPlan]

    class Config:
        orm_mode = True


class SubscriptionDetails(BaseModel):
    subscription_id: int

    class Config:
        orm_mode = True