import datetime
from pydantic import BaseModel
from typing import Optional


class Pangkat(BaseModel):
    id: Optional[int]
    pangkat: Optional[str]
    golongan: Optional[str]
    ruang: Optional[str]
    keterangan: Optional[str]
    creator: Optional[int]
    created_at: Optional[datetime.datetime]
    editor: Optional[int]
    updated_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class PangkatIn(BaseModel):
    golongan: str
    ruang: str
    pangkat: str
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

    class Config:
        orm_mode = True
