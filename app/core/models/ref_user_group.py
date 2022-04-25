from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.core.database import Base


class RefUserGroup(Base):
    __tablename__ = "ref_user_group"

    id = Column(Integer, primary_key=True, index=True)
    group_name = Column(String(50), unique=True, nullable=False, index=True)
    group_description = Column(String(225))