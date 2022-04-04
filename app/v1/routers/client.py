from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import db_session
from app.core.utils.auth import get_current_active_user
from app.core.models.user import User

router = APIRouter()


@router.get("/")
async def hello(current_user: User = Depends(get_current_active_user)):
    return {"data": current_user}


@router.post("/gaji/")
async def hello(current_user: User = Depends(get_current_active_user)):
    return {"data": current_user}