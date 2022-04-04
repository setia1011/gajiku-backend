from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.core.database import Base


class RefUserIdType(Base):
    __tablename__ = "ref_user_id_type"

    id = Column(Integer, primary_key=True, index=True)
    id_type = Column(String(50), unique=True, nullable=False, index=True)
    id_description = Column(String(225))

    # ref_user = relationship('User', backref='ref_user_id_type')