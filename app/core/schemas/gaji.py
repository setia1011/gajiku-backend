import datetime
from pydantic import BaseModel
from typing import Optional


class Pangkat(BaseModel):
    id: Optional[int]
    pangkat: Optional[str]
    golongan: Optional[str]
    ruang: Optional[str]
    keterangan: Optional[str]
    project_id: Optional[int]
    creator: Optional[int]
    created_at: Optional[datetime.datetime]
    editor: Optional[int]
    updated_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class PangkatIn(BaseModel):
    pangkat: str
    golongan: str
    ruang: str
    project_id: int
    keterangan: Optional[str]

    class Config:
        orm_mode = True


class Jabatan(BaseModel):
    id: Optional[int]
    kode: Optional[str]
    jabatan: Optional[str]
    kategori: Optional[str]
    besaran: Optional[float]
    jenis_besaran: Optional[str]
    dasar_penetapan: Optional[str]
    mulai_berlaku: Optional[str]
    selesai_berlaku: Optional[str]
    keterangan: Optional[str]
    project_id: Optional[int]
    status: Optional[str]
    creator: Optional[int]
    created_at: Optional[datetime.datetime]
    editor: Optional[int]
    updated_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class JabatanIn(BaseModel):
    kategori: str
    kode: str
    jabatan: str
    besaran: float
    jenis_besaran: str
    project_id: int
    keterangan: Optional[str]

    class Config:
        orm_mode = True


class Kawin(BaseModel):
    id: Optional[int]
    kode: Optional[str]
    keterangan: Optional[str]
    tunjangan_is: Optional[float]
    tunjangan_anak: Optional[float]
    tunjangan_beras: Optional[float]
    ptkp: Optional[float]

    dasar_penetapan: Optional[str]
    mulai_berlaku: Optional[str]
    selesai_berlaku: Optional[str]

    project_id: Optional[int]
    status: Optional[str]
    creator: Optional[int]
    created_at: Optional[datetime.datetime]
    editor: Optional[int]
    updated_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class KawinIn(BaseModel):
    kode: str
    keterangan: Optional[str]
    ptkp: float
    project_id: int

    class Config:
        orm_mode = True


# class Gaji(BaseModel):
#     id: Optional[int]
#     pangkat_id: Optional[int]
#     masa_kerja: Optional[int]
#     pokok: Optional[float]
#     dasar_penetapan: Optional[str]
#     mulai_berlaku: Optional[str]
#     selesai_berlaku: Optional[str]
#     keterangan: Optional[str]
#     project_id: Optional[int]
#     status: Optional[str]
#     creator: Optional[int]
#     created_at: Optional[datetime.datetime]
#     editor: Optional[int]
#     updated_at: Optional[datetime.datetime]
#
#     class Config:
#         orm_mode = True
#
#
# class GajiIn(BaseModel):
#     pangkat_id: int
#     masa_kerja: int
#     pokok: float
#     project_id: int
#
#     class Config:
#         orm_mode = True


class Gaji(BaseModel):
    gaji_pokok: Optional[float]
    tunjangan_istri: Optional[float]
    tunjangan_anak: Optional[float]
    tunjangan_beras: Optional[float]
    tunjangan_daerah: Optional[float]
    tunjangan_terpencil: Optional[float]
    tunjangan_jabatan_struktural: Optional[float]
    tunjangan_jabatan_fungsional: Optional[float]
    tunjangan_khusus_pajak: Optional[float]
    total: Optional[float]

    class Config:
        orm_mode = True


class Potongan(BaseModel):
    taspen: Optional[float]
    bpjs: Optional[float]
    sewa_rumah: Optional[float]
    biaya_jabatan: Optional[float]
    pph_21: Optional[float]
    kelebihan_gaji: Optional[float]
    total: Optional[float]

    class Config:
        orm_mode = True


class GajiOut(BaseModel):
    id: Optional[str]
    pangkat: Optional[str]
    golongan: Optional[str]
    ruang: Optional[str]
    masa_kerja: Optional[int]
    periode: Optional[str]
    gaji: Optional[Gaji]
    potongan: Optional[Potongan]
    netto: Optional[float]


class GajiIn(BaseModel):
    id: str
    bulan: int
    tahun: int
    jabatan: Optional[str]
    project_id: int
    pangkat: str
    masa_kerja: int
    status_kawin: str
    bpjs: str

    class Config:
        orm_mode = True


# class Potongan(BaseModel):
#     pph_21: Optional[float]
#
#     class Config:
#         orm_mode = True
#
#
# class PotonganIn(BaseModel):


