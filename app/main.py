from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.v1 import api
# from app.v0 import routers as v0


def get_application():
    _app = FastAPI(
        title=settings.PROJECT_NAME,
        description="API backend aplikasi GAJIKU",
        version="0.0.1",
        terms_of_service="https://gajiku.techack.id/terms/",
        contact={
            "name": "Aliyatus Saadah, Dwi Harsoyo, Setiadi, Aji Jumatara",
            "url": "https://gajiku.techack.id/contact/",
            "email": "gajiku@techack.id",
        },
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()

app.include_router(api.router_v1)
