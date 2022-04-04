from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import db_session

router = APIRouter()


@router.get("/subscribe/")
async def subscribe():
    return {"data": "This is user api"}