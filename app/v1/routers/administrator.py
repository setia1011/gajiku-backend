from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import db_session
from app.core.utils import auth
from app.core.models.user import User
from app.core.schemas import user as schema_user
from app.v1.services import user as service_user


router = APIRouter()


@router.get("/list-user/", response_model=list[schema_user.UserDetailOut], status_code=status.HTTP_200_OK)
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


@router.post("/user-detail/", response_model=schema_user.UserDetailOut, dependencies=[Depends(auth.default)], status_code=status.HTTP_200_OK)
async def user_detail(user: schema_user.FindUserByUsername, db: Session = Depends(db_session)):
    try:
        dt_user = service_user.find_user_by_username_3(username=user.username, db=db)
        return dt_user
    except Exception:
        raise
    finally:
        db.close()


@router.put("/update-group/", response_model=schema_user.UserDetailOut, dependencies=[Depends(auth.default)], status_code=status.HTTP_200_OK)
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


@router.put("/activate-subscribe/")
async def activate_subscribe():
    return {}