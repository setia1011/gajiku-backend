import datetime
from fastapi import Depends
from sqlalchemy.orm import Session, selectinload
from app.core.models import User, RefUserGroup, RefUserIdType
from app.core.schemas import playground


def user_login(username: str, password: str, db: Session = Depends):
    dt_user = db.query(User).filter(User.username == username, User.password == password).first()
    return dt_user


def find_user_by_username(username: str, db: Session = Depends):
    dt_user = db.query(User).filter(User.username == username).first()
    return dt_user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def find_user_by_username_2(username: str, db: Session = Depends):
    dt_user = db.query(User).filter(User.username == username)\
        .options(selectinload(User.ref_group)).options(selectinload(User.ref_id_type)).first()
    return dt_user

