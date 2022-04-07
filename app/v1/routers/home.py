from fastapi import APIRouter
from app.core.schemas import home

router = APIRouter()


@router.get("/", response_model=home.HomeInfoOut)
async def home():
    data = {"data": "Welcome! You are at home API now.."}
    return data