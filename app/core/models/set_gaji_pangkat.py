from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, Enum, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class SetGajiPangkat(Base):
    __tablename__ = "set_gaji_pangkat"

    id = Column(Integer, primary_key=True, index=True)
    kode = Column(String(50), nullable=False, index=True)
    keterangan = Column(String(500), index=True)
    client_id = Column(Integer, ForeignKey("tbl_client.id"), nullable=False, index=True)
    creator = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    editor = Column(Integer)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    ref_client = relationship("Client", backref="set_gaji_pangkat")