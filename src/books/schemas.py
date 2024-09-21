from pydantic import BaseModel
from datetime import date
from typing import Optional


class BookCreateRequest(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str


class BookUpdateRequest(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    published_date: Optional[date] = None
    page_count: Optional[int] = None
    language: Optional[str] = None