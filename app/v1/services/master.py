from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.models.set_gaji_pangkat import SetGajiPangkat


def create_golongan(golongan: str, ruang: str, pangkat: str, keterangan: str, db: Session = Depends):
    dt_golongan = SetGajiPangkat(golongan=golongan, ruang=ruang, pangkat=pangkat, keterangan=keterangan)
    return dt_golongan