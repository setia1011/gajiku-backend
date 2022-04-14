import datetime
from fastapi import Depends
from sqlalchemy.orm import Session, selectinload
from app.core.models import RefUserGroup


def list_ref_group(db: Session = Depends):
    dt_ref_group = db.query(RefUserGroup).all()
    return dt_ref_group

