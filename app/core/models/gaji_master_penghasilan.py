from sqlalchemy import Column, ForeignKey, String, Integer, TEXT, DateTime, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class GajiMasterPenghasilan(Base):
    __tablename__ = "tbl_gaji_master_penghasilan"

    id = Column(Integer, primary_key=True, index=True)
    penghasilan = Column(Integer, ForeignKey("set_gaji_penghasilan.id"), nullable=False, index=True)
    employee_id = Column(Integer, ForeignKey("tbl_gaji_employee.id"), nullable=False, index=True)
    client_id = Column(Integer, ForeignKey("tbl_client.id"), nullable=False, index=True)
    creator = Column(Integer, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    editor = Column(Integer, index=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), index=True)

    set_penghasilan = relationship("SetGajiPenghasilan", backref="tbl_gaji_master_penghasilan")
    ref_gaji_employee = relationship('GajiMasterEmployee', backref='tbl_gaji_master_penghasilan')
    ref_client = relationship("Client", backref="tbl_gaji_master_penghasilan")
