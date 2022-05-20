import pandas as pd

from fastapi import Depends
from sqlalchemy.orm import Session
from app.core import models
from app.core.config import settings


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
        (models.SetGajiPangkat.golongan == golongan) & (models.SetGajiPangkat.ruang == ruang) & (
                    models.SetGajiPangkat.project_id == project_id) | (
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
    dt_jabatan = models.SetGajiJabatan(kategori=kategori, kode=kode, jabatan=jabatan, besaran=besaran,
                                       jenis_besaran=jenis_besaran,
                                       keterangan=keterangan, project_id=project_id)
    return dt_jabatan


def find_jabatan(jabatan: str, project_id: int, db: Session = Depends):
    dt_jabatan = db.query(models.SetGajiJabatan).filter(models.SetGajiJabatan.jabatan == jabatan).filter(
        models.SetGajiJabatan.project_id == project_id).all()
    return dt_jabatan


def create_kawin(kode: str, keterangan: str, ptkp: float, project_id: int, db: Session = Depends):
    dt_kawin = models.SetGajiKawin(kode=kode, keterangan=keterangan, ptkp=ptkp, project_id=project_id)
    return dt_kawin


def create_gaji(pangkat_id: int, masa_kerja: int, pokok: float, project_id: int, db: Session = Depends):
    dt_gaji = models.SetGaji(pangkat_id=pangkat_id, masa_kerja=masa_kerja, pokok=pokok, project_id=project_id)
    return dt_gaji


def rincian_gaji(
        id: str,
        bulan: int,
        tahun: int,
        project_id: int,
        pangkat: str,
        masa_kerja: int,
        status_kawin: str,
        jabatan: str,
        bpjs: str,
        db: Session = Depends):
    a = models.SetGaji
    b = models.SetGajiPangkat
    c = models.SetGajiKawin
    d = models.SetGajiJabatan
    e = models.SetGajiBpjs

    pokok = db.query(a.pokok, b.golongan, b.pangkat, b.ruang).filter(a.pangkat_id == b.id).where(
        (a.project_id == project_id) & (a.masa_kerja == masa_kerja) & (b.pangkat == pangkat)).first()
    kawin = db.query(c.tunjangan_is, c.tunjangan_anak, c.tunjangan_beras, c.ptkp).where(
        (c.project_id == project_id) & (c.kode == status_kawin)).first()
    jabatan = db.query(d.besaran, d.kategori).where((d.kode == jabatan) & (d.project_id == project_id)).first()
    iuran_bpjs = db.query(e.besaran).where((e.kelas==bpjs) & (e.project_id==project_id)).first()


    gaji = {}
    if pokok:
        gaji['gaji_pokok'] = pokok[0]
        gaji['tunjangan_istri'] = pokok[0] * kawin[0] / 100
        gaji['tunjangan_anak'] = (pokok[0] * kawin[1] / 100) * 2
    if jabatan:
        if jabatan[1] == 'fungsional':
            gaji['tunjangan_jabatan_struktural'] = None
            gaji['tunjangan_jabatan_fungsional'] = jabatan[0]
        else:
            gaji['tunjangan_jabatan_struktural'] = jabatan[0]
            gaji['tunjangan_jabatan_fungsional'] = None
        gaji['tunjangan_beras'] = float(10 * 90000 * 3)

    js_bulan = settings.CORE_PATH + "/data/bulan.json"
    df_bulan = pd.read_json(js_bulan, typ='series')
    periode = None
    for val in df_bulan.iteritems():
        if val[0] == bulan:
            periode = str(val[1]) + ' ' + str(tahun)

    gaji['total'] = sum([x for x in gaji.values() if x is not None])

    potongan = {}
    potongan['taspen'] = round((4.75 / 100) * (gaji['gaji_pokok'] + gaji['tunjangan_istri'] + gaji['tunjangan_anak']), 0)
    if iuran_bpjs:
        potongan['bpjs'] = iuran_bpjs[0]
    else:
        potongan['bpjs'] = None
    potongan['pph_21'] = None

    # Biaya Jabatan
    if (5/100) * gaji['total'] > 500000:
        potongan['biaya_jabatan'] = 500000
    else:
        potongan['biaya_jabatan'] = round((5/100) * gaji['total'])

    potongan['total'] = sum([x for x in potongan.values() if x is not None])

    # Netto
    netto = round(gaji['total'] + potongan['total'], -3)

    # PKP Setahun
    if (netto * 12) - kawin[3] > 0:
        pkp = (netto * 12) - kawin[3]
    else:
        pkp = 0.0

    # PPh Pasal 21
    if 0.0 <= pkp <= 50000000:
        potongan['pph_21'] = (pkp * (5/100)) / 12
    elif 50000000 < pkp <= 250000000:
        potongan['pph_21'] = (pkp * (15/100)) / 12
    elif 250000000 < pkp <= 500000000:
        potongan['pph_21'] = (pkp * (25 / 100)) / 12
    else:
        potongan['pph_21'] = (pkp * (30 / 100)) / 12

    # Convert to null
    if potongan['pph_21'] == 0.0 or pokok[1] == 'I' or pokok[1] == 'II':
        potongan['pph_21'] = None

    return {
        "id": id,
        "periode": periode,
        "pangkat": pokok[2],
        "golongan": pokok[1],
        "ruang": pokok[3],
        "masa_kerja": masa_kerja,
        "gaji": gaji,
        "potongan": potongan,
        "netto": netto
    }
