import datetime
from importlib.util import LazyLoader
from fastapi import Depends
from sqlalchemy.orm import Session, selectinload, subqueryload
from app.core.models import User, Activation, Project, Subscription


def list_project(user_id, db: Session = Depends):
    dt_project = db.query(Project).filter(Project.user_id == user_id).all()
    return dt_project


def find_project(project_id: int, db: Session = Depends):
    dt_project = db.query(Project).filter(Project.id == project_id).first()
    return dt_project


def project_details(user_id: int, project_id: int, db: Session = Depends):
    dt_project = db.query(Project).filter(Project.user_id == user_id).filter(Project.id == project_id).first()
    return dt_project


def project_details_v2(user_id: int, project_id: int, db: Session = Depends):
    # dt_project = db.query(Project).filter(Project.id == project_id).filter(Project.user_id == user_id) \
    #     .options(selectinload(Project.ref_subscription), selectinload(Project.ref_id_type)).options().first()

    dt_project_v2 = db.query(Project).\
        filter(Project.id == project_id).\
            filter(Project.user_id == user_id).options(
            selectinload(Project.ref_subscription), 
            selectinload(Project.ref_id_type),
            subqueryload(Project.ref_subscription).\
                subqueryload(Subscription.ref_subscription_plan)).all()

    return dt_project_v2


def subscription_details(user_id: int, subs_id: int, db: Session = Depends):
    dt_subscription = db.query(Subscription).filter(Subscription.id == subs_id).filter(Subscription.creator == user_id) \
        .options(selectinload(Subscription.ref_project), selectinload(Subscription.ref_subscription_plan)).first()
    return dt_subscription


def update_project(
        id: int,
        project: str,
        address: str,
        responsible_name: str,
        responsible_id_type: int,
        responsible_id_number: str,
        db: Session = Depends):
    dt_project = Project(
        id=id,
        project=project,
        address=address,
        responsible_name=responsible_name,
        responsible_id_type=responsible_id_type,
        responsible_id_number=responsible_id_number)
    return dt_project


def extend_subscription(
        project_id: int,
        subs_month: int,
        subs_plan_id: int,
        db: Session = Depends):
    dt_subscription = Project(id=project_id, subs_plan_id=subs_plan_id, subs_month=subs_month)
    return dt_subscription
