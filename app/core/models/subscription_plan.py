from sqlalchemy import Column, ForeignKey, String, Integer, TEXT, DateTime, Enum, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class SubscriptionPlan(Base):
    __tablename__ = "tbl_subscription_plan"

    id = Column(Integer, primary_key=True, index=True)
    # basic, standard, premium
    plan = Column(Enum('basic', 'standard', 'premium'), index=True)
    # monthly price
    monthly_price = Column(Float, nullable=False, index=True)
    status = Column(Enum('valid', 'expired'))
    creator = Column(Integer, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    editor = Column(Integer, index=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), index=True)