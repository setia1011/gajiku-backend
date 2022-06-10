import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import db_session
from app.core.utils import auth
from app.core.models.user import User
from app.core.schemas import responses as schema_responses
from app.core.schemas import user as schema_user
from app.v1.services import user as service_user
from app.v1.services import administrator as service_administrator
from app.core.schemas import administrator as schema_administrator
from dateutil.relativedelta import relativedelta


router = APIRouter()


@router.get("/list-user/", response_model=list[schema_user.UserDetailOut], dependencies=[Depends(auth.admin)], status_code=status.HTTP_200_OK)
async def list_user(db: Session = Depends(db_session)):
    user_list = service_user.user_list(db=db)
    try:
        if not user_list:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="List data pengguna tidak ditemukan",
            )
        return user_list
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Terjadi kesalahan dari sistem"
        )
    finally:
        db.close()


@router.post("/user-detail/", response_model=schema_user.UserDetailOut, dependencies=[Depends(auth.admin)], status_code=status.HTTP_200_OK)
async def user_detail(user: schema_user.FindUserByUsername, db: Session = Depends(db_session)):
    try:
        dt_user = service_user.find_user_by_username_3(username=user.username, db=db)
        return dt_user
    except Exception:
        raise
    finally:
        db.close()


@router.put("/update-group/", response_model=schema_user.UserDetailOut, dependencies=[Depends(auth.admin)], status_code=status.HTTP_200_OK)
async def update_group(schema: schema_user.GroupUpdate, current_user: User = Depends(auth.get_current_active_user), db: Session = Depends(db_session)):
    try:
        current_user.group_id = schema.group_id
        update_data = schema.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(current_user, key, value)
        db.add(current_user)
        db.commit()

        dt_user = service_user.find_user_by_username_3(username=current_user.username, db=db)
        return dt_user
    except Exception:
        raise
    finally:
        db.close()


@router.put("/activate-subscription/", response_model=schema_responses.Simple, dependencies=[Depends(auth.admin)], status_code=status.HTTP_200_OK)
async def activate_subscription(
        subs: schema_administrator.ActivateSubscription,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    try:
        dt_subs = service_administrator.find_subscription_by_id(subs_id=subs.subs_id, db=db)
        if not dt_subs:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Data subscription tidak valid"
            )

        subs_start = datetime.datetime.now()
        subs_end = subs_start + relativedelta(months=dt_subs.subs_month)

        if dt_subs.status == 'pending':
            dt_subs.status = 'active'
            dt_subs.editor = current_user.id
            dt_subs.subs_start = subs_start
            dt_subs.subs_end = subs_end
            db.add(dt_subs)
            db.commit()
            db.refresh(dt_subs)
            if dt_subs.status == 'active':
                data = {"data": "Subcription berhasil diaktifkan"}
            else:
                data = {"data": "Terjadi kesalahan di sistem"}
        elif dt_subs.status == "active":
            data = {"data": "Subscription sudah pernah diaktifkan sebelumnya"}
        else:
            data = {"data": "Status subscription expired"}
        return data
    except Exception:
        raise
    finally:
        db.close()
