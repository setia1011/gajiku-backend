from fastapi import APIRouter
from app.v1.routers import \
    user, \
    settings, \
    subscription, \
    client, \
    playground, \
    home, \
    administrator, \
    gaji, \
    reference


router_v1 = APIRouter()
router_v1.include_router(home.router, prefix="", tags=["home"])
router_v1.include_router(user.router, prefix="/v1/user", tags=["user"])
router_v1.include_router(client.router, prefix="/v1/client", tags=["client"])
router_v1.include_router(administrator.router, prefix="/v1/administrator", tags=["administrator"])
router_v1.include_router(subscription.router, prefix="/v1/subscription", tags=["subscription"])
router_v1.include_router(gaji.router, prefix="/v1/gaji", tags=["gaji"])
router_v1.include_router(settings.router, prefix="/v1/settings", tags=["settings"])
router_v1.include_router(playground.router, prefix="/v1/playground", tags=["playground"])
router_v1.include_router(reference.router, prefix="/v1/reference", tags=["reference"])