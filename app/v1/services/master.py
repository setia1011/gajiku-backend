from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.models.set_gaji_pangkat import SetGajiPangkat


def create_pangkat(
        golongan: str,
        ruang: str,
        pangkat: str,
        keterangan: str,
        db: Session = Depends):
    dt_pangkat = SetGajiPangkat(
        golongan=golongan,
        ruang=ruang,
        pangkat=pangkat,
        keterangan=keterangan)
    return dt_pangkat


def find_pangkat(golongan, ruang, pangkat, db: Session = Depends):
    dt = db.query(SetGajiPangkat).where((SetGajiPangkat.golongan == golongan) & (SetGajiPangkat.ruang == ruang) | (SetGajiPangkat.pangkat == pangkat)).all()
    # dt = db.query(SetGajiPangkat).filter(SetGajiPangkat.golongan == golongan).filter(SetGajiPangkat.ruang == ruang).first()
    return dt
