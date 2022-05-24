from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import db_session
from app.core.models.user import User
from app.v1.services import gaji as service_gaji
from app.core.schemas import gaji as schema_gaji
from app.core.utils import auth


router = APIRouter()


@router.post("/pangkat/", response_model=schema_gaji.Pangkat, dependencies=[Depends(auth.client)])
async def pangkat(
        schema: schema_gaji.PangkatIn,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    try:
        dt = service_gaji.find_pangkat(golongan=schema.golongan, ruang=schema.ruang, pangkat=schema.pangkat, project_id=schema.project_id, db=db)
        if dt:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Data pangkat sudah ada di sistem")

        dt_pangkat = service_gaji.create_pangkat(
            golongan=schema.golongan,
            pangkat=schema.pangkat,
            ruang=schema.ruang,
            keterangan=schema.keterangan,
            project_id=schema.project_id,
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


@router.post("/jabatan/", response_model=schema_gaji.Jabatan, dependencies=[Depends(auth.client)])
async def jabatan(schema: schema_gaji.JabatanIn, current_user: User = Depends(auth.get_current_active_user), db: Session = Depends(db_session)):
    try:
        dt = service_gaji.find_jabatan(kode=schema.kode, project_id=schema.project_id, db=db)
        if dt:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Data jabatan sudah ada di sistem")

        dt_jabatan = service_gaji.create_jabatan(
            kategori=schema.kategori,
            kode=schema.kode,
            jabatan=schema.jabatan,
            besaran=schema.besaran,
            jenis_besaran=schema.jenis_besaran,
            project_id=schema.project_id,
            keterangan=schema.keterangan,
            db=db
        )
        dt_jabatan.creator = current_user.id
        db.add(dt_jabatan)
        db.commit()
        db.refresh(dt_jabatan)
        return dt_jabatan
    except Exception:
        raise
    finally:
        db.close()
    return {}


@router.post("/status-kawin/", response_model=schema_gaji.Kawin, dependencies=[Depends(auth.client)])
async def status_kawin(schema: schema_gaji.KawinIn, current_user: User = Depends(auth.get_current_active_user), db: Session = Depends(db_session)):
    dt_kawin = service_gaji.create_kawin(kode=schema.kode, keterangan=schema.keterangan, ptkp=schema.ptkp, project_id=schema.project_id, db=db)
    dt_kawin.creator = current_user.id
    db.add(dt_kawin)
    db.commit()
    db.refresh(dt_kawin)
    return dt_kawin


# @router.post("/perjadin/")
# async def perjadin():
#     return {}
#
#
# @router.post("/grade/")
# async def grade():
#     return {}
#
#
# @router.post("/bpjs/")
# async def bpjs():
#     return {}


@router.post("/rincian-gaji", response_model=schema_gaji.GajiOut)
async def rincian_gaji(gaji: schema_gaji.GajiIn, db: Session = Depends(db_session)):
    try:
        dt = service_gaji.rincian_gaji(
            id=gaji.id,
            bulan=gaji.bulan,
            tahun=gaji.tahun,
            jabatan=gaji.jabatan,
            project_id=gaji.project_id,
            pangkat=gaji.pangkat,
            masa_kerja=gaji.masa_kerja,
            status_kawin=gaji.status_kawin,
            bpjs=gaji.bpjs,
            db=db)
        return dt
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Terjadi kesalahan")
    finally:
        db.close()
