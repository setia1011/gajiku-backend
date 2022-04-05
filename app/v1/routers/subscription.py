import datetime
from dateutil.relativedelta import relativedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import db_session
from app.core.schemas import subcription as sch_subs
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
        subs: sch_subs.SubscribePlan,
        db: Session = Depends(db_session)):
    try:
        subscription_plan = serv_subs.plan(subs_plan_id=subs.subs_plan_id, db=db)
        if not subscription_plan:
            raise HTTPException(
                detail="Data subscription plan tidak valid",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        subs_price = subscription_plan.monthly_price * subs.subs_month
        ppn = subs_price * 10 / 100
        total_subs_price = subs_price + ppn
        subs_end = subs.subs_start + relativedelta(months=subs.subs_month)

        dt_subscription_plan = serv_subs.subscribe_plan(
            subs_plan_id=subs.subs_plan_id,
            subs_month=subs.subs_month,
            subs_start=subs.subs_start,
            subs_price=total_subs_price,
            subs_end=subs_end,
            creator=subs.creator,
            db=db)
        db.add(dt_subscription_plan)
        db.commit()
        db.refresh(dt_subscription_plan)

        return {"data": dt_subscription_plan}
    except Exception:
        raise
    finally:
        db.close()


@router.put("/upgrade-plan/")
async def upgrade_plan():
    return {"data": "Upgrade subscription plan"}


@router.post("/cancel-plan/")
async def cancel_plan():
    return {"data": "Cancel subscription plan"}
