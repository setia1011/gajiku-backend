from sqlalchemy import Column, String, Integer
from app.core.database import Base


class RefProvinsi(Base):
    __tablename__ = "ref_provinsi"

    id = Column(Integer, primary_key=True, index=True)
    provinsi = Column(String(500), index=True)