from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import db_session
from app.core.models.user import User
from app.core.utils import auth
from app.core.schemas import user as schema_user
from app.v1.services import user as service_user

router = APIRouter()


@router.post("/register-client/", response_model=schema_user.UserDetailOut, dependencies=[Depends(auth.default)], status_code=status.HTTP_200_OK)
async def register_client(
        client: schema_user.RegisterClient,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    try:
        # Check if client already exists
        dt_client = service_user.find_client_exists(name=client.name, db=db)
        if dt_client:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Client dengan nama {client.name} sudah ada di dalam sistem"
            )

        dt_client = service_user.register_client(
            name=client.name,
            address=client.address,
            responsible_name=client.responsible_name,
            responsible_id_type=client.responsible_id_type,
            responsible_id_number=client.responsible_id_number,
            creator=client.creator,
            db=db)
        db.add(dt_client)
        db.commit()
        db.refresh(dt_client)

        # Update client_id in table user
        if dt_client:
            current_user.client_id = dt_client.id
            db.add(current_user)
            db.commit()

            dt_user = service_user.find_user_by_username_3(username=current_user.username, db=db)

            return dt_user
        db.rollback()
    except Exception:
        # db.rollback()
        raise
    finally:
        db.close()