from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import db_session
from app.core.utils.auth import get_password_hash
from app.core.config import settings
from app.core.models.user import User
from app.v1.services import master as service_master
from app.core.schemas import master as schema_master
from app.core.utils import auth


router = APIRouter()


@router.post("/pangkat/", response_model=schema_master.Pangkat, dependencies=[Depends(auth.default)])
async def pangkat(
        schema: schema_master.PangkatIn,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    try:
        dt = service_master.find_pangkat(golongan=schema.golongan, ruang=schema.ruang, pangkat=schema.pangkat, db=db)
        if dt:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Data pangkat sudah ada di sistem")

        dt_pangkat = service_master.create_pangkat(
            golongan=schema.golongan,
            pangkat=schema.pangkat,
            ruang=schema.ruang,
            keterangan=schema.keterangan,
            db=db
        )
        dt_pangkat.creator = current_user.id
        db.add(dt_pangkat)
        db.commit()
        db.refresh(dt_pangkat)
        return dt_pangkat
    except Exception:
        raise
    finally:
        db.close()


@router.post("/jabatan/")
async def jabatan():
    return {}


@router.post("/grade/")
async def grade():
    return {}


@router.post("/bpjs/")
async def bpjs():
    return {}


@router.post("/status-kawin/")
async def status_kawin():
    return {}


@router.post("/perjadin/")
async def perjadin():
    return {}


@router.post("/penghasilan/")
async def penghasilan():
    return {}


@router.post("/potongan/")
async def potongan():
    return {}
