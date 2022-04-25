import datetime
from pydantic import BaseModel
from typing import Optional


class Golongan(BaseModel):
    id: Optional[int]
    golongan: Optional[str]
    ruang: Optional[str]
    pangkat: Optional[str]
    keterangan: Optional[str]
    project_id: Optional[int]
    creator: Optional[int]
    created_at: Optional[datetime.datetime]
    editor: Optional[int]
    updated_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class GolonganIn(BaseModel):
    golongan: str
    ruang: str
    pangkat: str
    keterangan: Optional[str]
    project_id: int

    class Config:
        orm_mode = True
