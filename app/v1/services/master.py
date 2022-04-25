from fastapi import Depends
from sqlalchemy.orm import Session
from app.core import models


def create_pangkat(
        golongan: str,
        ruang: str,
        pangkat: str,
        keterangan: str,
        db: Session = Depends):
    dt_pangkat = models.SetGajiPangkat(
        golongan=golongan,
        ruang=ruang,
        pangkat=pangkat,
        keterangan=keterangan)
    return dt_pangkat


def find_pangkat(golongan, ruang, pangkat, db: Session = Depends):
    dt_pangkat = db.query(models.SetGajiPangkat).where((models.SetGajiPangkat.golongan == golongan) & (models.SetGajiPangkat.ruang == ruang) | (models.SetGajiPangkat.pangkat == pangkat)).all()
    return dt_pangkat


def create_jabatan(
    kategori: str,
    jabatan: str,
    besaran: str,
    jenis_besaran: str,
    keterangan: str,
    db: Session = Depends):
    dt_jabatan = models.SetGajiJabatan(kategori=kategori, jabatan=jabatan, besaran=besaran, jenis_besaran=jenis_besaran, keterangan=keterangan)
    return dt_jabatan
