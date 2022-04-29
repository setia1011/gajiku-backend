from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, Enum, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class SetGajiBpjs(Base):
    __tablename__ = "set_gaji_bpjs"

    id = Column(Integer, primary_key=True, index=True)
    kelas = Column(String(50), nullable=False, index=True)

    besaran = Column(Float, index=True)
    jenis_besaran = Column(Enum("persentase", "spesifik"), nullable=False, index=True)
    dasar_penetapan = Column(String(500))
    mulai_berlaku = Column(DateTime(timezone=True))
    selesai_berlaku = Column(DateTime(timezone=True))
    keterangan = Column(String(500), index=True)
    project_id = Column(Integer, ForeignKey("tbl_project.id"), nullable=False, index=True)
    status = Column(Enum("berlaku", "tidak berlaku"), nullable=False, server_default="berlaku", index=True)

    creator = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    editor = Column(Integer)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
