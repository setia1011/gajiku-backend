import datetime
from fastapi import Depends
from sqlalchemy.orm import Session, selectinload
from app.core.models import User, Activation, Project


def list_project(user_id, db: Session = Depends):
    dt_project = db.query(Project).filter(Project.user_id == user_id).all()
    return dt_project


def project_detail(user_id: int, project_id: int, db: Session = Depends):
    dt_project = db.query(Project).filter(Project.user_id == user_id).filter(Project.id == project_id).first()
    return dt_project
