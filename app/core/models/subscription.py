from sqlalchemy import Column, ForeignKey, String, Integer, TEXT, DateTime, Float, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Subscription(Base):
    __tablename__ = "tbl_subscription"

    id = Column(Integer, primary_key=True, index=True)
    subs_plan_id = Column(Integer, ForeignKey('tbl_subscription_plan.id'), nullable=False, index=True)
    subs_month = Column(Integer, nullable=False, index=True)
    subs_price = Column(Float, nullable=False, index=True)
    subs_start = Column(DateTime(timezone=True), index=True)
    subs_end = Column(DateTime(timezone=True), index=True)

    token = Column(String(255), unique=True, nullable=False)
    project_id = Column(Integer, ForeignKey("tbl_project.id"), nullable=False, index=True)
    status = Column(Enum("pending","active","expired","canceled"), server_default="pending", nullable=False, index=True)

    creator = Column(Integer, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    editor = Column(Integer, index=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), index=True)

    ref_subscription_plan = relationship('SubscriptionPlan', backref='tbl_subscription')
    ref_project = relationship("Project", backref="tbl_subscription")