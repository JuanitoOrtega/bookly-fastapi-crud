from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from src.books.schemas import BookCreateRequest, BookUpdateRequest
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.services import BookService
from src.books.responses import BookResponse
from src.db.main import get_session
from typing import List

book_router = APIRouter()
book_service = BookService()


@book_router.get('/', response_model=List[BookResponse])
async def get_all_books(session: AsyncSession = Depends(get_session)) -> List[dict]:
    books = await book_service.get_all_books(session)
    return books


@book_router.post('/', status_code=status.HTTP_201_CREATED, response_model=BookResponse)
async def create_book(book_data: BookCreateRequest, session: AsyncSession = Depends(get_session)) -> dict:
    new_book = await book_service.create_book(book_data, session)
    return new_book


@book_router.get('/{book_uid}', response_model=BookResponse)
async def get_book_by_id(book_uid: str, session: AsyncSession = Depends(get_session)):
    book = await book_service.get_book_by_uid(book_uid, session)
    if book:
        book.uid = str(book.uid)
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')


@book_router.patch('/{book_uid}', response_model=BookResponse)
async def update_book(book_uid: str, book_update_data: BookUpdateRequest, session: AsyncSession = Depends(get_session)):
    update_book = await book_service.update_book(book_uid, book_update_data, session)
    
    if not update_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')
    
    update_book.uid = str(update_book.uid)
    return update_book


@book_router.delete('/{book_uid}', status_code=status.HTTP_200_OK)
async def delete_book(book_uid: str, session: AsyncSession = Depends(get_session)):
    deleted = await book_service.delete_book(book_uid, session)
    
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')
    
    return {"message": "Book deleted successfully"}