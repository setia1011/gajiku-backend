from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.models.set_gaji_pangkat import SetGajiPangkat


def create_golongan(
        golongan: str,
        ruang: str,
        pangkat: str,
        keterangan: str,
        project_id: int,
        db: Session = Depends):
    dt_golongan = SetGajiPangkat(
        golongan=golongan,
        ruang=ruang,
        pangkat=pangkat,
        keterangan=keterangan,
        project_id=project_id)
    return dt_golongan