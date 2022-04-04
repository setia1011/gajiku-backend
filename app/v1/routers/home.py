from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def home():
    return {"data": "Welcome! You are at home API now.."}