from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.models import RefGroup, RefIdType, User, SubscriptionPlan, RefProvinsi


def create_provinsi(
        provinsi: str,
        db: Session = Depends):
    dt_provinsi = RefProvinsi(provinsi=provinsi)
    return dt_provinsi


def create_user_group(
        group_name: str,
        group_description: str,
        db: Session = Depends):
    dt_group = RefGroup(group_name=group_name, group_description=group_description)
    return dt_group


def create_id_type(
        id_type: str,
        id_description: str, db: Session = Depends):
    dt_id_type = RefIdType(id_type=id_type, id_description=id_description)
    return dt_id_type


def create_user(
        name: str,
        username: str,
        password: str,
        email: str,
        group: str,
        db: Session = Depends):
    dt_user = User(name=name, username=username, password=password, email=email, group=group)
    return dt_user


def create_superuser(
        name: str,
        username: str,
        password: str,
        email: str,
        group_id: int,
        status: str,
        db: Session = Depends):
    dt_user = User(name=name, username=username, password=password, email=email, group_id=group_id, status=status)
    return dt_user


def create_subscription_plan(
    plan: str, monthly_price: str, status: str, creator: int, db: Session = Depends):
    dt_subscription_plan = SubscriptionPlan(plan=plan, monthly_price=monthly_price, status=status, creator=creator)
    return dt_subscription_plan