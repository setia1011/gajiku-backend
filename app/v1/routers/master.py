from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import db_session
from app.core.utils.auth import get_password_hash
from app.core.config import settings
from app.core.utils.auth import get_current_active_user
from app.v1.services import master as service_master
from app.core.schemas import master as schema_master


router = APIRouter()


@router.post("/golongan/", response_model=schema_master.Golongan)
async def golongan(schema: schema_master.GolonganIn, db: Session = Depends(db_session)):
    dt_golongan = service_master.create_golongan(
        golongan=schema.golongan,
        pangkat=schema.pangkat,
        ruang=schema.ruang,
        keterangan=schema.keterangan,
        project_id=schema.project_id,
        db=db
    )
    db.add(dt_golongan)
    db.commit()
    data = db.refresh(dt_golongan)
    return data


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
