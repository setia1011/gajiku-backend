from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import db_session
from app.v1.services import reference as service_reference
from app.core.schemas import reference as schema_reference
from app.core.utils import auth, useful
from app.core.utils.auth import get_current_active_user
from app.core.schemas import responses as schema_responses
from app.core.schemas.reference import Group, UserIdType
from app.core.models.user import User


router = APIRouter()


@router.post("/group/", response_model=schema_responses.Simple, status_code=status.HTTP_200_OK)
async def group(
        settings_schema: Group,
        db: Session = Depends(db_session),
        current_user: User = Depends(get_current_active_user)):
    try:
        # Create user groups
        user_group = service_reference.create_user_group(
            group_name=settings_schema.group_name,
            group_description=settings_schema.group_description,
            db=db)
        db.add(user_group)
        db.commit()
        db.refresh(user_group)
        data = {"data": "Berhasil menambahkan grup"}
        return data
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


@router.get("/list-group/", response_model=list[schema_reference.RefGroup], dependencies=[Depends(auth.admin)], status_code=status.HTTP_200_OK)
async def list_group(db: Session = Depends(db_session)):
    dt_ref_group = service_reference.list_ref_group(db=db)
    return dt_ref_group


@router.post("/id-type/", response_model=schema_responses.Simple, status_code=status.HTTP_200_OK)
async def id_type(
        settings_schema: UserIdType,
        db: Session = Depends(db_session),
        current_user: User = Depends(get_current_active_user)):
    try:
        # Create id types
        id_type = service_reference.create_id_type(
            id_type=settings_schema.id_type,
            id_description=settings_schema.id_description,
            db=db)
        db.add(id_type)
        db.commit()
        db.refresh(id_type)
        data = {"data": "Berhasil menambahkan jenis ID"}
        return data
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


@router.get("/list-id-type/", response_model=list[schema_reference.RefIdType], dependencies=[Depends(auth.default)], status_code=status.HTTP_200_OK)
async def list_id_type(db: Session = Depends(db_session)):
    dt_ref_id_type = service_reference.list_id_type(db=db)
    return dt_ref_id_type


@router.get("/id-type/{s}", response_model=list[schema_reference.RefIdType])
async def find_id_type(s=str, db: Session = Depends(db_session)):
    dt = service_reference.find_id_type(s=s, db=db)
    return dt