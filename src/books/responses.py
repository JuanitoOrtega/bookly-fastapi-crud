from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class BookResponseModel(BaseModel):
    uid: str
    title: str
    author: str
    publisher: str
    published_date: Optional[date]
    page_count: Optional[int]
    language: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True