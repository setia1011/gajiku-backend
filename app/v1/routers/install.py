import pandas as pd
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import db_session
from app.core.utils.auth import get_password_hash
from app.core.config import settings
from app.core.schemas import responses as schema_responses
from app.v1.services import install as service_reference


router = APIRouter()


@router.post("/db-initial/", response_model=schema_responses.Simple, status_code=status.HTTP_200_OK)
async def db_initial(db: Session = Depends(db_session)):
    # Insert provinsi
    provinsi = settings.CORE_PATH + "/data/provinsi.csv"
    df_provinsi = pd.read_csv(provinsi, usecols=["provinsi"])
    for i, val in df_provinsi.iterrows():
        dt_provinsi = service_reference.create_provinsi(
            provinsi=val['provinsi'],
            db=db)
        db.add(dt_provinsi)
        db.commit()
        db.refresh(dt_provinsi)

    # Insert groups
    groups = settings.CORE_PATH + "/data/groups.csv"
    df_groups = pd.read_csv(groups, usecols=["group_name","group_description"])
    for i, val in df_groups.iterrows():
        user_group = service_reference.create_user_group(
            group_name=val['group_name'],
            group_description=val['group_description'],
            db=db)
        db.add(user_group)
        db.commit()
        db.refresh(user_group)

    # Insert id types
    id_types = settings.CORE_PATH + "/data/id_types.csv"
    df_id_types = pd.read_csv(id_types, usecols=["id_type", "id_description"])
    for i, val in df_id_types.iterrows():
        user_id_type = service_reference.create_id_type(
            id_type=val['id_type'],
            id_description=val['id_description'],
            db=db)
        db.add(user_id_type)
        db.commit()
        db.refresh(user_id_type)

    # Insert superuser
    superuser = settings.CORE_PATH + "/data/superuser.csv"
    df_superuser = pd.read_csv(superuser, usecols=["name","username","password","email","group_id"])
    for i, val in df_superuser.iterrows():
        user_superuser = service_reference.create_superuser(
            name=val['name'],
            username=val['username'],
            password=get_password_hash(str(val['password'])),
            email=val['email'],
            group_id=val['group_id'],
            status="enabled",
            db=db)
        db.add(user_superuser)
        db.commit()
        db.refresh(user_superuser)

    # Insert subscription plan
    subscription_plan = settings.CORE_PATH + "/data/subscription_plan.csv"
    df_subscription_plan = pd.read_csv(subscription_plan, usecols=['plan','monthly_price','status','creator'])
    for i, val in df_subscription_plan.iterrows():
        _subscription_plan = service_reference.create_subscription_plan(
            plan=val['plan'],
            monthly_price=val['monthly_price'],
            status=val['status'],
            creator=val['creator'],
            db=db)
        db.add(_subscription_plan)
        db.commit()
        db.refresh(_subscription_plan)

    data = {"data": "Install data berhasil"}
    return data