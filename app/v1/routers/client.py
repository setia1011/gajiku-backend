from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import db_session
from app.core.models.user import User
from app.core.utils import auth, useful
from app.core.schemas import user as schema_user
from app.core.schemas import client as schema_client
from app.v1.services import user as service_user
from app.v1.services import client as service_client
from app.core.schemas import subcription as sch_subs
from app.v1.services import subscription as serv_subs
from dateutil.relativedelta import relativedelta


router = APIRouter()


@router.post("/register-project/", response_model=schema_user.UserDetailOut, dependencies=[Depends(auth.default)], status_code=status.HTTP_200_OK)
async def register_project(
        client: schema_user.RegisterClient,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    try:
        # Check if client already exists
        dt_client = service_user.find_client_exists(project=client.project, db=db)
        if dt_client:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Client dengan nama {client.project} sudah ada di dalam sistem"
            )

        dt_client = service_user.register_client(
            project=client.project,
            address=client.address,
            responsible_name=client.responsible_name,
            responsible_id_type=client.responsible_id_type,
            responsible_id_number=client.responsible_id_number,
            user_id=current_user.id,
            creator=current_user.id,
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


@router.get("/list-project/", response_model=list[schema_client.Client], status_code=status.HTTP_200_OK)
async def list_project(current_user: User = Depends(auth.get_current_active_user), db: Session = Depends(db_session)):
    dt_project = service_client.list_project(user_id=current_user.id, db=db)
    return dt_project


@router.post("/project-detail/", response_model=schema_client.Client, status_code=status.HTTP_200_OK)
async def project_detail(
        client: schema_client.ProjectDetail,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    dt_project = service_client.project_detail(user_id=current_user.id, client_id=client.id, db=db)
    return dt_project


@router.post("/subscribe-plan/")
async def subscribe_plan(
        subs: sch_subs.SubscribePlan,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    try:
        subscription_plan = serv_subs.plan(subs_plan_id=subs.subs_plan_id, db=db)
        if not subscription_plan:
            raise HTTPException(
                detail="Data subscription plan tidak valid",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        client = service_client.project_detail(user_id=current_user.id, client_id=subs.project_id, db=db)
        if not client:
            raise HTTPException(
                detail="Data client tidak valid",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        subs_price = subscription_plan.monthly_price * subs.subs_month
        ppn = subs_price * 10 / 100
        total_subs_price = subs_price + ppn
        subs_end = subs.subs_start + relativedelta(months=subs.subs_month)
        token = useful.random_string(16)

        dt_subscription_plan = serv_subs.subscribe_plan(
            subs_plan_id=subs.subs_plan_id,
            subs_month=subs.subs_month,
            subs_start=subs.subs_start,
            subs_price=total_subs_price,
            subs_end=subs_end,
            token=token,
            client_id=client.id,
            creator=current_user.id,
            db=db)
        db.add(dt_subscription_plan)
        db.commit()
        db.refresh(dt_subscription_plan)

        return {"data": dt_subscription_plan}
    except Exception:
        raise
    finally:
        db.close()