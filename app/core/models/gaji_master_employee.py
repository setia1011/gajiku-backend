from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class GajiMasterEmployee(Base):
    __tablename__ = "tbl_gaji_employee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, index=True)
    id_number = Column(String(50), nullable=False, index=True)
    id_type = Column(Integer, ForeignKey("ref_user_id_type.id"), nullable=False, index=True)

    jabatan_id = Column(Integer, ForeignKey("set_gaji_jabatan.id"), index=True)
    # pangkat_id = Column(Integer, ForeignKey("set_gaji_pangkat.id"), index=True)
    golongan_id = Column(Integer, ForeignKey("set_gaji_golongan.id"), index=True)
    grade_id = Column(Integer, ForeignKey("set_gaji_grade.id"), index=True)
    masa_kerja = Column(Integer, index=True)
    bpjs_id = Column(Integer, ForeignKey("set_gaji_bpjs.id"), index=True)

    status_kawin = Column(Integer, nullable=False, index=True)
    status_bekerja = Column(Enum("aktif", "tidak aktif"), nullable=False, index=True)
    client_id = Column(Integer, ForeignKey("tbl_client.id"), nullable=False, index=True)
    creator = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    editor = Column(Integer)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    set_jabatan = relationship('SetGajiJabatan', backref='tbl_gaji_employee')
    # set_pangkat = relationship('SetGajiPangkat', backref='tbl_gaji_employee')
    set_golongan = relationship('SetGajiGolongan', backref='tbl_gaji_employee')
    set_grade = relationship('SetGajiGrade', backref='tbl_gaji_employee')
    set_bpjs = relationship('SetGajiBpjs', backref='tbl_gaji_employee')