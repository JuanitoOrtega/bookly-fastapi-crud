from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
import uuid


class BaseResponse(BaseModel):
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class BookResponse(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: Optional[date]
    page_count: Optional[int]
    language: Optional[str]
    created_at: datetime
    updated_at: datetime