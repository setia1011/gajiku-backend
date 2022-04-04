from sqlalchemy import Column, ForeignKey, String, Integer, Enum, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.core.utils.useful import dayday


class Activation(Base):
    __tablename__ = "tbl_activation"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('tbl_user.id'), nullable=False, index=True)
    acticode = Column(String(255), unique=True, nullable=False)
    expired = Column(DateTime(timezone=True))
    activated_at = Column(DateTime(timezone=True), onupdate=func.now())
    status = Column(Enum('activated', 'inactivated'), nullable=False, server_default='inactivated')

    ref_user = relationship('User',  backref="tbl_activation")