from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, Enum, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class SetGajiPerjadin(Base):
    __tablename__ = "set_gaji_perjadin"

    id = Column(Integer, primary_key=True, index=True)
    golongan_id = Column(Integer, ForeignKey("set_gaji_golongan.id"), nullable=False, index=True)
    uang_harian = Column(Float, index=True)
    jenis_besaran = Column(Enum("persentase", "spesifik"), nullable=False, index=True)
    provinsi_id = Column(Integer, ForeignKey("ref_provinsi.id"), nullable=False, index=True)
    dasar_penetapan = Column(String(500))
    mulai_berlaku = Column(DateTime(timezone=True))
    selesai_berlaku = Column(DateTime(timezone=True))
    status = Column(Enum("berlaku", "tidak berlaku"), nullable=False, server_default="berlaku", index=True)
    client_id = Column(Integer, ForeignKey("tbl_client.id"), nullable=False, index=True)
    creator = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    editor = Column(Integer)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    ref_client = relationship("Client", backref="set_gaji_perjadin")
    ref_golongan = relationship("SetGajiGolongan", backref="set_gaji_perjadin")
    ref_provinsi = relationship("RefProvinsi", backref="set_gaji_perjadin")