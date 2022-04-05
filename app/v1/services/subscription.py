import datetime
from fastapi import Depends
from sqlalchemy.orm import Session, selectinload
from app.core.models.subscription_plan import SubscriptionPlan


def list_plan(db: Session = Depends):
    dt_subscription_plan = db.query(SubscriptionPlan).all()
    return dt_subscription_plan