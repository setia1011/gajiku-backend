import datetime
from fastapi import Depends
from sqlalchemy.orm import Session, selectinload
from app.core.models.subscription_plan import SubscriptionPlan
from app.core.models.subscription import Subscription


def plan(subs_plan_id: int, db: Session = Depends):
    dt_subscription_plan = db.query(SubscriptionPlan).filter(SubscriptionPlan.id == subs_plan_id).first()
    return dt_subscription_plan


def list_plan(db: Session = Depends):
    dt_subscription_plan = db.query(SubscriptionPlan).all()
    return dt_subscription_plan


def subscribe(client_id: int, db: Session = Depends):
    dt_subscribe = db.query(Subscription).filter(Subscription.client_id == client_id).filter(Subscription.status == "pending").all()
    return dt_subscribe


def subscribe_plan(
        subs_plan_id: int,
        subs_month: int,
        subs_start: datetime.datetime,
        subs_end: datetime.datetime,
        subs_price: float,
        token: str,
        client_id: int,
        creator: int,
        db: Session = Depends):
    dt_subscription_plan = Subscription(
        subs_plan_id=subs_plan_id,
        subs_month=subs_month,
        subs_start=subs_start,
        subs_end=subs_end,
        subs_price=subs_price,
        token=token,
        client_id=client_id,
        creator=creator)
    return dt_subscription_plan
