from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import db_session

router = APIRouter()


@router.get("/list-plan/")
async def list_plan():
    return {"data": "List subscription plan"}


@router.get("/detail-plan/{subs_plan_id}")
async def detail_plan(subs_plan_id: int):
    return {"data": f"Detail subscription plan {subs_plan_id}"}


@router.post("/register-plan/")
async def register_plan():
    return {"data": "Register subscription plan"}


@router.put("/upgrade-plan/")
async def upgrade_plan():
    return {"data": "Upgrade subscription plan"}


@router.post("/cancel-plan/")
async def cancel_plan():
    return {"data": "Cancel subscription plan"}
