import datetime
from fastapi import Depends
from sqlalchemy.orm import Session, selectinload
from app.core.models import User, Activation, Client, Subscription


def find_subscription_by_id(subs_id: int, db: Session = Depends):
    dt_subs = db.query(Subscription).filter(Subscription.id==subs_id).first()
    return dt_subs


def activate_subscribe(subs_id, status: str, db: Session = Depends):
    dt_subs = Subscription(subs_id=subs_id, status=status)
    return dt_subs
