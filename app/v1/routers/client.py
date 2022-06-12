import datetime

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


@router.post("/register-project/", response_model=schema_user.UserDetailOut, dependencies=[Depends(auth.default)],
             status_code=status.HTTP_200_OK)
async def register_project(project: schema_user.RegisterProject,
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

        token = useful.random_string(16)

        dt_project = service_user.register_project(
            project=project.project,
            token=token,
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
    dt_project = service_project.project_details(user_id=current_user.id, project_id=project.project_id, db=db)
    return dt_project


@router.post('/project-details-v2/', response_model=schema_project.ProjectDetailsOutV2, status_code=status.HTTP_200_OK)
async def project_details_v2(
        project: schema_project.ProjectDetail,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    dt_project = service_project.project_details_v2(user_id=current_user.id, project_id=project.project_id, db=db)
    return dt_project


@router.post('/project-details-v3/', status_code=status.HTTP_200_OK)
async def project_details_v3(
        project: schema_project.ProjectDetail,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    dt_project = service_project.project_details_v2(user_id=current_user.id, project_id=project.project_id, db=db)
    dx = dt_project.ref_subscription

    lendx = len(dx)
    du = {}
    subs_month = 0
    for i in range(lendx):
        du['plan_id'] = dx[i].subs_plan_id
        du['plan'] = dx[i].ref_subscription_plan.plan
        subs_month += dx[i].subs_month
        du['status'] = dx[i].status
        if i == 0:
            du['subs_start'] = dx[i].subs_start
        if i == lendx - 1:
            du['subs_end'] = dx[i].subs_end
    du['subs_month'] = subs_month
    dt_project.ref_subscription.subs_month = 0

    return dt_project


@router.post('/subscription-details/', response_model=schema_project.SubscriptionDetailsOut,
             status_code=status.HTTP_200_OK)
async def subscription_details(
        subscribe: schema_project.SubscriptionDetails,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    dt_subscription = service_project.subscription_details(user_id=current_user.id, subs_id=subscribe.subscription_id,
                                                           db=db)
    return dt_subscription


@router.post('/update-project', response_model=schema_project.Project, status_code=status.HTTP_200_OK)
async def update_project(
        project: schema_project.ProjectUpdateIn,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    dt_project = service_project.find_project(project_id=project.project_id, db=db)
    if not dt_project:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Data tidak valid")

    dt_project.editor = current_user.id
    update_data = project.dict(exclude_unset=True, exclude_none=True)
    for key, value in update_data.items():
        # Skip null or empty value
        if value:
            setattr(dt_project, key, value)
    db.add(dt_project)
    db.commit()
    db.refresh(dt_project)
    return dt_project


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

        project = service_project.project_details(user_id=current_user.id, project_id=subs.project_id, db=db)
        if not project:
            raise HTTPException(
                detail="Data project tidak valid",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        # Kalau masih punya subs pending ga boleh subs baru
        dt_subscribe = serv_subs.subscribe_pending(project_id=project.id, db=db)
        if dt_subscribe:
            raise HTTPException(
                detail="Anda masih mempunyai project dengan status pending",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        subs_price = subscription_plan.monthly_price * subs.subs_month
        ppn = subs_price * 10 / 100
        total_subs_price = subs_price + ppn

        dt_subscription_plan = serv_subs.subscribe_plan(
            subs_plan_id=subs.subs_plan_id,
            subs_month=subs.subs_month,
            subs_price=total_subs_price,
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


@router.post("/extend-subscription/", response_model=sch_subs.Subscription)
async def extend_subscription(
        subs: sch_subs.SubscribePlan,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    try:
        # Cek subscribe active
        subs_active = serv_subs.subscribe_active(project_id=subs.project_id, db=db)
        if not subs_active:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tidak ditemukan data project aktif")

        # Cek subscribe pending
        subs_pending = serv_subs.subscribe_pending(project_id=subs.project_id, db=db)
        if subs_pending:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Anda masih mempunyai project dengan status pending")

        # Cek plan yang minta available di dalam tabel subscribe_plan
        subscription_plan = serv_subs.plan(subs_plan_id=subs.subs_plan_id, db=db)
        if not subscription_plan:
            raise HTTPException(
                detail="Data subscription plan tidak valid",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        # Cek project
        project = service_project.project_details(user_id=current_user.id, project_id=subs.project_id, db=db)
        if not project:
            raise HTTPException(
                detail="Data project tidak valid",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        subs_price = subscription_plan.monthly_price * subs.subs_month
        ppn = subs_price * 10 / 100
        total_subs_price = subs_price + ppn

        last_subs = subs_active[-1]
        subs_start = last_subs.subs_end + relativedelta(days=1)
        subs_end = subs_start + relativedelta(months=subs.subs_month)

        dt_subs_extend = serv_subs.extend_plan(
            subs_plan_id=subs.subs_plan_id,
            subs_month=subs.subs_month,
            subs_start=subs_start,
            subs_end=subs_end,
            subs_price=total_subs_price,
            project_id=project.id,
            creator=current_user.id,
            db=db)

        db.add(dt_subs_extend)
        db.commit()
        db.refresh(dt_subs_extend)

        return dt_subs_extend
    except Exception:
        raise
    finally:
        db.close()


@router.post("/upgrade-subscription/", include_in_schema=False)
async def upgrade_subscription(
        subs: sch_subs.SubscribePlanUpgrade,
        current_user: User = Depends(auth.get_current_active_user),
        db: Session = Depends(db_session)):
    # Cek subscribe active
    subs_active = serv_subs.subscribe_active(project_id=subs.project_id, db=db)
    if not subs_active:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tidak ditemukan data project aktif")

    # Cek subscribe pending
    subs_pending = serv_subs.subscribe_pending(project_id=subs.project_id, db=db)
    if subs_pending:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Anda masih mempunyai project dengan status pending")

    # Cek plan yang minta available di dalam tabel subscribe_plan
    subscription_plan = serv_subs.plan(subs_plan_id=subs.subs_plan_id, db=db)
    if not subscription_plan:
        raise HTTPException(
            detail="Data subscription plan tidak valid",
            status_code=status.HTTP_400_BAD_REQUEST
        )

    # Cek project
    project = service_project.project_details(user_id=current_user.id, project_id=subs.project_id, db=db)
    if not project:
        raise HTTPException(
            detail="Data project tidak valid",
            status_code=status.HTTP_400_BAD_REQUEST
        )

    subs_month = sum([subs_active[i].subs_month for i in range(len(subs_active))])

    subs_price = subscription_plan.monthly_price * subs_month
    ppn = subs_price * 10 / 100
    total_subs_price = subs_price + ppn

    total_price = sum([subs_active[i].subs_price for i in range(len(subs_active))])

    dt_subs_upgrade = serv_subs.subscribe_plan(
        subs_plan_id=subs.subs_plan_id,
        subs_month=subs_month,
        subs_price=total_subs_price,
        project_id=project.id,
        creator=current_user.id,
        db=db)

    # db.add(dt_subs_upgrade)
    # db.commit()
    # db.refresh(dt_subs_upgrade)

    return total_price

# @router.post("/billing-confirmation/")
# async def billing_confirmation():
#     return {}
