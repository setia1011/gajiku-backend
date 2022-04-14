from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import db_session
from app.v1.services import reference as service_reference
from app.core.schemas import reference as schema_reference
from app.core.utils import auth, useful


router = APIRouter()


@router.get("/group/", response_model=list[schema_reference.RefUserGroup], dependencies=[Depends(auth.admin)], status_code=status.HTTP_200_OK)
async def group(db: Session = Depends(db_session)):
    dt_ref_group = service_reference.list_ref_group(db=db)
    return dt_ref_group


@router.get("/id-type/", response_model=list[schema_reference.RefIdType], dependencies=[Depends(auth.default)], status_code=status.HTTP_200_OK)
async def id_type(db: Session = Depends(db_session)):
    dt_ref_id_type = service_reference.list_id_type(db=db)
    return dt_ref_id_type
