from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import db_session
from app.core.models.user import User
from app.core.utils import auth, useful
from app.core.schemas import user as schema_user
from app.core.schemas import project as schema_project
from app.v1.services import user as service_user
from app.v1.services import project as service_project
from app.core.schemas import subcription as sch_subs
from app.v1.services import subscription as serv_subs
from dateutil.relativedelta import relativedelta


router = APIRouter()


@router.post("/register-project/", response_model=schema_user.UserDetailOut, dependencies=[Depends(auth.default)], status_code=status.HTTP_200_OK)
async def register_project(
        project: schema_user.RegisterProject,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    try:
        # Check if project already exists
        dt_project = service_user.find_project_exists(project=project.project, db=db)
        if dt_project:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Project dengan nama {project.project} sudah ada di dalam sistem"
            )

        dt_project = service_user.register_project(
            project=project.project,
            address=project.address,
            responsible_name=project.responsible_name,
            responsible_id_type=project.responsible_id_type,
            responsible_id_number=project.responsible_id_number,
            user_id=current_user.id,
            creator=current_user.id,
            db=db)
        db.add(dt_project)
        db.commit()
        db.refresh(dt_project)

        # Update project_id in table user
        if dt_project:
            current_user.project_id = dt_project.id
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


@router.get("/list-project/", response_model=list[schema_project.Project], status_code=status.HTTP_200_OK)
async def list_project(current_user: User = Depends(auth.get_current_active_user), db: Session = Depends(db_session)):
    dt_project = service_project.list_project(user_id=current_user.id, db=db)
    return dt_project


@router.post("/project-details/", response_model=schema_project.Project, status_code=status.HTTP_200_OK)
async def project_details(
        project: schema_project.ProjectDetail,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    dt_project = service_project.project_detail(user_id=current_user.id, project_id=project.project_id, db=db)
    return dt_project


@router.post('/project-details-v2/', response_model=schema_project.ProjectDetailsOutV2, status_code=status.HTTP_200_OK)
async def project_details_v2(
        project: schema_project.ProjectDetail,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    dt_project = service_project.project_details_v2(user_id=current_user.id, project_id=project.project_id, db=db)
    return dt_project


@router.post('/subscription-details/', response_model=schema_project.SubscriptionDetailsOut, status_code=status.HTTP_200_OK)
async def subscription_details(
        subscribe: schema_project.SubscriptionDetails,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    dt_subscription = service_project.subscription_details(user_id=current_user.id, subs_id=subscribe.subscription_id, db=db)
    return dt_subscription


@router.post("/subscribe-plan/", response_model=sch_subs.Subscription)
async def subscribe_plan(
        subs: sch_subs.SubscribePlan,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    try:
        # Cek plan yang minta available di dalam tabel subscribe_plan
        subscription_plan = serv_subs.plan(subs_plan_id=subs.subs_plan_id, db=db)
        if not subscription_plan:
            raise HTTPException(
                detail="Data subscription plan tidak valid",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        project = service_project.project_detail(user_id=current_user.id, project_id=subs.project_id, db=db)
        if not project:
            raise HTTPException(
                detail="Data project tidak valid",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        # Kalau masih punya subs pending ga boleh subs baru
        dt_subscribe = serv_subs.subscribe(project_id=project.id, db=db)
        if dt_subscribe:
            raise HTTPException(
                detail="Anda masih mempunyai project dengan status pending",
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
            project_id=project.id,
            creator=current_user.id,
            db=db)
        db.add(dt_subscription_plan)
        db.commit()
        db.refresh(dt_subscription_plan)
        return dt_subscription_plan
    except Exception:
        raise
    finally:
        db.close()


# @router.post("/billing-confirmation/")
# async def billing_confirmation():
#     return {}

