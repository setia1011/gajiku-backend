import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import db_session
from app.v1.services import subscription as serv_subs


router = APIRouter()


@router.get("/plan/{subs_plan_id}")
async def plan(subs_plan_id: int, db: Session = Depends(db_session)):
    dt_subscription_plan = serv_subs.plan(subs_plan_id=subs_plan_id, db=db)
    return {"data": dt_subscription_plan}


@router.get("/list-plan/")
async def list_plan(db: Session = Depends(db_session)):
    dt_subscription_plan = serv_subs.list_plan(db=db)
    return {"data": dt_subscription_plan}


@router.post("/subscribe-plan/")
async def subscribe_plan(
        subs_plan_id: int,
        subs_month: int,
        subs_price: float,
        subs_start: datetime.datetime,
        subs_end: datetime.datetime,
        creator: int,
        db: Session = Depends(db_session)):
    dt_subscription_plan = serv_subs.subscribe_plan(
        subs_plan_id=subs_plan_id,
        subs_month=subs_month,
        subs_price=subs_price,
        subs_start=subs_start,
        subs_end=subs_end,
        creator=creator,
        db=db)
    db.add(dt_subscription_plan)
    db.commit()
    db.refresh(dt_subscription_plan)
    return {"data": dt_subscription_plan}


@router.put("/upgrade-plan/")
async def upgrade_plan():
    return {"data": "Upgrade subscription plan"}


@router.post("/cancel-plan/")
async def cancel_plan():
    return {"data": "Cancel subscription plan"}
