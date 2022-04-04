import datetime
from fastapi import Depends
from sqlalchemy.orm import Session, selectinload
from app.core.models import RefUserGroup, RefUserIdType, User, Activation


def create_user(
        name: str,
        username: str,
        password: str,
        email: str,
        db: Session = Depends):
    dt_user = User(name=name, username=username, password=password, email=email)
    return dt_user


def user_login(username: str, password: str, db: Session = Depends):
    dt_user = db.query(User).filter(User.username == username, User.password == password).first()
    return dt_user


def find_user_by_username(username: str, db: Session = Depends):
    dt_user = db.query(User).filter(User.username == username).first()
    return dt_user


def find_user_by_username_3(username: str, db: Session = Depends):
    dt_user = db.query(User).filter(User.username == username)\
        .options(selectinload(User.ref_group), selectinload(User.ref_id_type), selectinload(User.ref_client)).first()
    return dt_user


def find_user_by_username_2(username: str, db: Session = Depends):
    dt_user = db.query(User, RefUserGroup, RefUserIdType) \
        .join(RefUserGroup, RefUserGroup.id == User.group_id, isouter=True) \
        .join(RefUserIdType, RefUserIdType.id == User.id_type, isouter=True).filter(User.username == username).all()

    li = []
    ct = 0
    for i, j, k in dt_user:
        # First list
        li.append({"id": i.id})
        # Append to the first list
        li[ct]["name"] = i.name
        li[ct]["username"] = i.username
        # li[ct]["password"] = i.password
        li[ct]["id_type_id"] = i.id_type
        li[ct]["id_number"] = i.id_number
        if k:
            li[ct]["id_type"] = k.id_type
        else:
            li[ct]["id_type"] = None
        li[ct]["email"] = i.email
        li[ct]["phone"] = i.phone
        li[ct]["group_id"] = i.group_id
        li[ct]["group_name"] = j.group_name
        li[ct]["client_id"] = i.client_id
        li[ct]["address"] = i.address
        li[ct]["status"] = i.status
        ct += 1
    return li


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
                                     selectinload(User.ref_client)).all()
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
