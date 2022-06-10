import datetime
from fastapi import Depends
from sqlalchemy.orm import Session, selectinload
from app.core.models import User, Activation, Project


def create_user(
        name: str,
        username: str,
        password: str,
        email: str,
        db: Session = Depends):
    dt_user = User(name=name, username=username, password=password, email=email)
    return dt_user


def register_project(
        project: str,
        token: str,
        address: str,
        responsible_name: str,
        responsible_id_type: int,
        responsible_id_number: str,
        user_id: int,
        creator: int,
        db: Session = Depends):
    dt_project = Project(
        project=project,
        token=token,
        address=address,
        responsible_name=responsible_name,
        responsible_id_type=responsible_id_type,
        responsible_id_number=responsible_id_number,
        user_id=user_id,
        creator=creator)
    return dt_project


def user_login(username: str, password: str, db: Session = Depends):
    dt_user = db.query(User).filter(User.username == username, User.password == password).first()
    return dt_user


def find_project_exists(project: str, db: Session = Depends):
    dt_project = db.query(Project).filter(Project.project == project).first()
    return dt_project


def find_user_by_username(username: str, db: Session = Depends):
    dt_user = db.query(User).filter(User.username == username).first()
    return dt_user


def find_user_by_username_3(username: str, db: Session = Depends):
    dt_user = db.query(User).filter(User.username == username) \
        .options(selectinload(User.ref_group), selectinload(User.ref_id_type), selectinload(User.ref_project)).first()
    return dt_user


def find_user_by_id(id: int, db: Session = Depends):
    dt_user = db.query(User).filter(User.id == id).first()
    return dt_user


def update_password(
        username: str,
        password: str,
        db: Session = Depends):
    dt_user = User(username=username, password=password)
    return dt_user


def user_list(db: Session = Depends):
    dt_user = db.query(User).options(selectinload(User.ref_group),
                                     selectinload(User.ref_id_type),
                                     selectinload(User.ref_project)).all()
    return dt_user


def find_email(email: str, db: Session = Depends):
    dt_email = db.query(User).filter(User.email == email).first()
    return dt_email


def create_activation(
        acticode: str,
        user_id: int,
        expired: datetime,
        db: Session = Depends):
    dt_activation = Activation(user_id=user_id, acticode=acticode, expired=expired)
    return dt_activation


def find_acticode(acticode: str, db: Session = Depends):
    dt_activation = db.query(Activation).filter(Activation.acticode == acticode).first()
    return dt_activation


def activation(status: str, db: Session = Depends):
    dt_activation = Activation(status=status)
    return dt_activation


def enable_user(status: str, db: Session = Depends):
    dt_user = User(status=status)
    return dt_user
