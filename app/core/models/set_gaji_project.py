from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, Enum, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class SetGajiProject(Base):
    __tablename__ = "set_gaji_project"

    id = Column(Integer, primary_key=True, index=True)
    set = Column(String(50), nullable=False, index=True)
    set_id = Column(String(500), index=True)
    project_id = Column(Integer, ForeignKey("tbl_project.id"), nullable=False, index=True)
    creator = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    editor = Column(Integer)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    ref_project = relationship("Project", backref="set_gaji_project")
