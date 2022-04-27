from fastapi import Depends
from sqlalchemy.orm import Session
from app.core import models


def create_gaji_project(set: str, set_id: int, project_id: int, db: Session = Depends):
    dt_gaji_project = models.SetGajiProject(set=set, set_id=set_id, project_id=project_id)
    return dt_gaji_project


def create_pangkat(
        golongan: str,
        ruang: str,
        pangkat: str,
        keterangan: str,
        project_id: int,
        db: Session = Depends):
    dt_pangkat = models.SetGajiPangkat(
        golongan=golongan,
        ruang=ruang,
        pangkat=pangkat,
        keterangan=keterangan,
        project_id=project_id)
    return dt_pangkat


def find_pangkat(golongan, ruang, pangkat, project_id, db: Session = Depends):
    dt_pangkat = db.query(models.SetGajiPangkat).where(
        (models.SetGajiPangkat.golongan == golongan) & (models.SetGajiPangkat.ruang == ruang) & (models.SetGajiPangkat.project_id == project_id) | (
                    models.SetGajiPangkat.pangkat == pangkat)).all()
    return dt_pangkat


def create_jabatan(
        kategori: str,
        kode: str,
        jabatan: str,
        besaran: str,
        jenis_besaran: str,
        keterangan: str,
        project_id: int,
        db: Session = Depends):
    dt_jabatan = models.SetGajiJabatan(kategori=kategori, kode=kode, jabatan=jabatan, besaran=besaran, jenis_besaran=jenis_besaran,
                                       keterangan=keterangan, project_id=project_id)
    return dt_jabatan


def find_jabatan(jabatan: str, project_id: int, db: Session = Depends):
    dt_jabatan = db.query(models.SetGajiJabatan).filter(models.SetGajiJabatan.jabatan == jabatan).filter(models.SetGajiJabatan.project_id == project_id).all()
    return dt_jabatan


def create_kawin(kode: str, keterangan: str, ptkp: float, project_id: int, db: Session = Depends):
    dt_kawin = models.SetGajiKawin(kode=kode, keterangan=keterangan, ptkp=ptkp, project_id=project_id)
    return dt_kawin


def create_gaji(pangkat_id: int, masa_kerja: int, pokok: float, project_id: int, db: Session = Depends):
    dt_gaji = models.SetGaji(pangkat_id=pangkat_id, masa_kerja=masa_kerja, pokok=pokok, project_id=project_id)
    return dt_gaji


def pokok(
        name: str,
        project_id: int,
        pangkat: str,
        masa_kerja: int,
        status_kawin: str,
        jabatan: str,
        db: Session = Depends):
    a = models.SetGaji
    b = models.SetGajiPangkat
    c = models.SetGajiKawin
    d = models.SetGajiJabatan

    pokok = db.query(a.pokok).filter(a.pangkat_id==b.id).where((a.project_id==project_id) & (a.masa_kerja==masa_kerja) & (b.pangkat==pangkat)).first()
    kawin = db.query(c.tunjangan_is, c.tunjangan_anak, c.tunjangan_beras).where((c.project_id==project_id) & (c.kode==status_kawin)).first()
    jabatan = db.query(d.besaran, d.kategori).where((d.kode==jabatan) & (d.project_id==project_id)).first()

    gaji = {}
    gaji['name'] = name
    gaji['gaji_pokok'] = pokok[0]
    gaji['tunjangan_istri'] = pokok[0] * kawin[0] / 100
    gaji['tunjangan_anak'] = (pokok[0] * kawin[1] / 100) * 2
    if jabatan[1] == 'fungsional':
        gaji['tunjangan_jabatan_struktural'] = None
        gaji['tunjangan_jabatan_fungsional'] = jabatan[0]
    else:
        gaji['tunjangan_jabatan_struktural'] = jabatan[0]
        gaji['tunjangan_jabatan_fungsional'] = None
    gaji['tunjangan_beras'] = float(10 * 90000 * 3)

    return gaji
