import datetime
from fastapi import Depends
from sqlalchemy.orm import Session, selectinload
from app.core.models import User, Activation, Client


def list_project(user_id, db: Session = Depends):
    dt_project = db.query(Client).filter(Client.user_id == user_id).all()
    return dt_project


def project_detail(user_id: int, client_id: int, db: Session = Depends):
    dt_project = db.query(Client).filter(Client.user_id == user_id).filter(Client.id == client_id).first()
    return dt_project
