import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# Core
from app.core.utils.auth import create_access_token
from app.core.database import db_session
from app.core.schemas import user as schema_user
from app.core.utils import auth
from app.core.utils import email
from app.core.utils.useful import dayday, acticode, current_datetime

# Services
from app.v1.services import user as service_user

# Models
from app.core.models.user import User
from app.v1.services.user import find_user_by_username_2

router = APIRouter()


@router.post("/login/", status_code=status.HTTP_200_OK)
async def login(user: schema_user.UserLogin, db: Session = Depends(db_session)):
    dt_user = service_user.find_user_by_username(username=user.username, db=db)
    # ensure the user exist in the system
    if not dt_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Data user tidak ditemukan di dalam sistem",
        )
    # verify password
    if not auth.verify_password(user.password, dt_user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password yang digunakan tidak sesuai",
        )
    return {
        "access_token": create_access_token(sub=dt_user.username),
        "token_type": "bearer"
    }


@router.post("/register/", status_code=status.HTTP_201_CREATED)
async def register_user(
        user: schema_user.UserRegister,
        db: Session = Depends(db_session)):
    try:
        # Check username duplicate
        dt_new = service_user.find_user_by_username(username=user.username, db=db)
        if dt_new:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Silahkan menggunakan username yang lain"
            )

        # Check if email exists
        dt_email = service_user.find_email(email=user.email, db=db)
        if dt_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Silahkan menggunakan email yang lain",
            )

        # Create user
        dt_user = service_user.create_user(
            name=user.name,
            username=user.username,
            password=auth.get_password_hash(user.password),
            email=user.email,
            db=db
        )
        db.add(dt_user)
        db.commit()
        db.refresh(dt_user)

        acticodex = acticode(6)
        expired = dayday(3)
        dt_activation = service_user.create_activation(
            user_id=dt_user.id,
            acticode=acticodex,
            expired=expired
        )
        db.add(dt_activation)
        if dt_activation:
            # Send acticode to register email
            email.send(
                email=user.email,
                name=user.name,
                code=acticodex,
                expired=expired
            )
        db.commit()
        return {"data": "Kode aktivasi telah dikirimkan ke email, segera lakukan aktivasi"}
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


@router.put("/update-profile/", dependencies=[Depends(auth.default)], status_code=status.HTTP_201_CREATED)
async def update_user(
        user: schema_user.UserUpdate,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    try:
        if not current_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Data tidak valid")
        current_user.editor = current_user.id
        update_data = user.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(current_user, key, value)
        db.add(current_user)
        db.commit()
        db.refresh(current_user)
        return {"data": "Berhasil melakukan update data profil"}
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


@router.put("/update-group/", dependencies=[Depends(auth.default)], status_code=status.HTTP_201_CREATED)
async def update_group(
        schema: schema_user.GroupUpdate,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    try:
        current_user.group_id = schema.group_id
        update_data = schema.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(current_user, key, value)

        db.add(current_user)
        db.commit()
        dt_user = find_user_by_username_2(username=current_user.username, db=db)
        return {"data": dt_user}
    except Exception:
        raise
    finally:
        db.close()


@router.patch("/update-password/", status_code=status.HTTP_201_CREATED)
async def update_password(
        schema: schema_user.UpdatePassword,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    try:
        dt_user = service_user.find_user_by_username(username=current_user.username, db=db)
        # ensure the user exist in the system
        if not dt_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Data user tidak ditemukan di dalam sistem",
            )
        # verify new password with confirm new password
        if schema.old_password == schema.new_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password lama tidak boleh sama dengan password baru",
            )
        # verify new password with confirm new password
        if schema.new_password != schema.confirm_new_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password baru tidak sama dengan password konfirmasi",
            )
        # verify old password
        if not auth.verify_password(schema.old_password, dt_user.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password lama tidak sesuai",
            )
        # update with the new password
        dt_user.password = auth.get_password_hash(schema.new_password)
        db.add(dt_user)
        db.commit()
        db.refresh(dt_user)
        return {"data": "Berhasil melakukan update password"}
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


@router.post("/activation/", status_code=status.HTTP_200_OK)
async def user_activation(schema: schema_user.Activation, db: Session = Depends(db_session)):
    dt_activation = service_user.find_acticode(acticode=schema.acticode, db=db)
    if not dt_activation:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Kode aktivasi tidak valid",
        )

    if dt_activation.status == 'activated':
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Kode aktivasi sudah pernah diaktifkan sebelumnya",
        )

    dt_user = service_user.find_user_by_id(id=dt_activation.user_id, db=db)
    if not dt_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Kode aktivasi tidak valid",
        )

    a = dt_activation.expired
    b = datetime.datetime.strptime(current_datetime(), "%Y-%d-%m %H:%M:%S")
    if a >= b:
        try:
            dt_activation.status = 'activated'
            db.add(dt_activation)
            db.commit()
            db.refresh(dt_activation)

            dt_user.status = 'enabled'
            db.add(dt_user)
            db.commit()
            db.refresh(dt_user)
            response = "Aktivasi berhasil"
        except Exception:
            db.rollback()
            raise
        finally:
            db.close()
    else:
        response = "Kode aktivasi sudah tidak berlaku"
    return {"data": response}


@router.get("/list/", response_model=list[schema_user.ReadUserDetail], status_code=status.HTTP_200_OK)
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
        raise
    finally:
        db.close()


@router.post("/user-detail/", response_model=schema_user.ReadUserDetail, dependencies=[Depends(auth.default)], status_code=status.HTTP_200_OK)
async def user_detail(user: schema_user.FindUserByUsername, db: Session = Depends(db_session)):
    try:
        dt_user = service_user.find_user_by_username_3(username=user.username, db=db)
        return dt_user
    except Exception:
        raise
    finally:
        db.close()
