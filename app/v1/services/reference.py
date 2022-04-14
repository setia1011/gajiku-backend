import datetime
from fastapi import Depends
from sqlalchemy.orm import Session, selectinload
from app.core.models import RefUserGroup, RefUserIdType


def list_ref_group(db: Session = Depends):
    dt_ref_group = db.query(RefUserGroup).all()
    return dt_ref_group


def list_id_type(db: Session = Depends):
    dt_ref_id_type = db.query(RefUserIdType).all()
    return dt_ref_id_type

