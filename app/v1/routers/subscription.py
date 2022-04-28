import datetime
from dateutil.relativedelta import relativedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import db_session
from app.core.schemas import subcription as sch_subs
from app.v1.services import subscription as serv_subs


router = APIRouter()


# @router.post("/plan/", status_code=status.HTTP_200_OK)
# async def plan():
#     return {}


@router.get("/plan/{subs_plan_id}", response_model=sch_subs.SubscribeOut)
async def plan(subs_plan_id: int, db: Session = Depends(db_session)):
    dt_subscription_plan = serv_subs.plan(subs_plan_id=subs_plan_id, db=db)
    return dt_subscription_plan


@router.get("/list-plan/", response_model=list[sch_subs.SubscribeOut])
async def list_plan(db: Session = Depends(db_session)):
    dt_subscription_plan = serv_subs.list_plan(db=db)
    return dt_subscription_plan


# @router.put("/update-plan/")
# async def update_plan():
#     return {"data": "Update subscription plan"}
#
#
# @router.post("/cancel-plan/")
# async def cancel_plan():
#     return {"data": "Cancel subscription plan"}
