import datetime
from pydantic import BaseModel
from typing import Optional


class Pangkat(BaseModel):
    id: Optional[int]
    pangkat: Optional[str]
    golongan: Optional[str]
    ruang: Optional[str]
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


class PangkatIn(BaseModel):
    golongan: str
    ruang: str
    pangkat: str
    besaran: float
    jenis_besaran: str
    keterangan: Optional[str]

    class Config:
        orm_mode = True
