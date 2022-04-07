import datetime

from pydantic import BaseModel
from typing import Optional


class HomeInfoOut(BaseModel):
    data: str

