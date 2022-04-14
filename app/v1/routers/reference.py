from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import db_session
from app.v1.services import reference as service_reference
from app.core.schemas import reference as schema_reference

router = APIRouter()


@router.get("/group/", response_model=list[schema_reference.RefUserGroup], status_code=status.HTTP_200_OK)
async def group(db: Session = Depends(db_session)):
    dt_ref_group = service_reference.list_ref_group(db=db)
    return dt_ref_group
