from sqlalchemy import Column, ForeignKey, String, Integer, TEXT, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Project(Base):
    __tablename__ = "tbl_project"

    id = Column(Integer, primary_key=True, index=True)
    project = Column(String(255), nullable=False, index=True)
    address = Column(TEXT)
    responsible_name = Column(String(50), nullable=False)
    responsible_id_type = Column(Integer, ForeignKey('ref_id_type.id'), nullable=False, index=True)
    responsible_id_number = Column(String(50), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("tbl_user.id"), nullable=False, index=True)
    creator = Column(Integer, index=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    editor = Column(Integer)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    ref_id_type = relationship('RefIdType', backref='tbl_project')
