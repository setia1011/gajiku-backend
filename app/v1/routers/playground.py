from typing import List, Union
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import db_session
from app.core.utils import auth
from app.core.models import User, RefGroup, RefIdType
from app.core.schemas import playground
from app.v1.services import playground as crud_play

router = APIRouter()


@router.get("/decode-token/", dependencies=[Depends(auth.superuser)])
async def decode_tokens(current_user: User = Depends(auth.get_current_active_user)):
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjQ5MzIwNTQ4LCJpYXQiOjE2NDg2MjkzNDgsInN1YiI6InNldGlhIn0.I60xVYgFMOuxTcKsRR-xYDi5jE1Gg5q6ZeNdkgYrX54"
    decoded_token = auth.decode_token(access_token)
    return {"data": decoded_token}


@router.get("/user-detail/", dependencies=[Depends(auth.superuser)])
async def user_detail(db: Session = Depends(db_session)):
    _user_detail = db.query(User, RefGroup, RefIdType) \
        .join(RefGroup, RefGroup.id == User.group_id, isouter=True) \
        .join(RefIdType, RefIdType.id == User.id_type, isouter=True).all()

    li = []
    ct = 0
    for i, j, k in _user_detail:
        # First list
        li.append({"id": i.id})
        # Append to the first list
        li[ct]["name"] = i.name
        li[ct]["username"] = i.username
        li[ct]["password"] = i.password
        li[ct]["id_type_id"] = i.id_type
        li[ct]["id_number"] = i.id_number
        if k:
            li[ct]["id_type"] = k.id_type
        else:
            li[ct]["id_type"] = None
        li[ct]["email"] = i.email
        li[ct]["phone"] = i.phone
        li[ct]["group_id"] = i.group_id
        li[ct]["group_name"] = j.group_name
        li[ct]["project_id"] = i.project_id
        li[ct]["address"] = i.address
        li[ct]["status"] = i.status
        ct += 1
    return {"data": li}


@router.post("/test-response-model/", response_model=playground.UserOut)
async def test_response_model(user: playground.UserLogin, db: Session = Depends(db_session)):
    try:
        dt_user = crud_play.find_user_by_username(username=user.username, db=db)
        return dt_user
    except Exception:
        raise
    finally:
        db.close()


@router.post("/test-response-model-joined/", response_model=playground.ReadUserWithGroup)
async def test_response_model_joined(user: playground.UserIn2, db: Session = Depends(db_session)):
    try:
        dt_user = crud_play.find_user_by_username_2(username=user.username, db=db)
        return dt_user
    except Exception:
        raise
    finally:
        db.close()


