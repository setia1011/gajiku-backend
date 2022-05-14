import os
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    CORE_PATH = os.path.abspath(os.path.dirname(__file__))

    PROJECT_NAME: str = None
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    SMTP_USERNAME: str = None
    SMTP_PASSWORD: str = None
    SMTP_HOST: str = None
    SMTP_PORT: int = None

    JWT_SECRET: str = None
    JWT_ALGORITHM: str = None

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    MYSQL_USER: str = None
    MYSQL_PASSWORD: str = None
    MYSQL_HOST: str = None
    MYSQL_PORT: str = None
    MYSQL_DATABASE: str = None
    DATABASE_URI: Optional[str] = None

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return f"mysql://{values.get('MYSQL_USER')}:{values.get('MYSQL_PASSWORD')}@{values.get('MYSQL_HOST')}:" \
               f"{values.get('MYSQL_PORT')}/{values.get('MYSQL_DATABASE')}"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
