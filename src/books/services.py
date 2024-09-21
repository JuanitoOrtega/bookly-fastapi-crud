from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
from datetime import datetime

from .models import Book
from .schemas import BookCreateRequest, BookUpdateRequest


class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(statement)
        return result.all()

    async def get_book_by_uid(self, book_uid: str, session: AsyncSession):
        statement = select(Book).where(Book.uid == book_uid)
        result = await session.exec(statement)
        return result.first()
    
    async def create_book(self, book_data: BookCreateRequest, session: AsyncSession):
        book_data_dict = book_data.model_dump()
        
        if isinstance(book_data_dict['published_date'], str):
            book_data_dict['published_date'] = datetime.strptime(book_data_dict['published_date'], '%Y-%m-%d').date()
            
        new_book = Book(**book_data_dict)
        async with session.begin():
            session.add(new_book)
        return new_book
    
    async def update_book(self, book_uid: str, update_data: BookUpdateRequest, session: AsyncSession):
        book_to_update = await self.get_book_by_uid(book_uid, session)
        
        if book_to_update:
            update_data_dict = update_data.model_dump()
            
            # Solo actualiza los campos que no sean None
            for key, value in update_data_dict.items():
                if value is not None:
                    setattr(book_to_update, key, value)
                    
            await session.commit()
            return book_to_update
        else:
            return None
    
    async def delete_book(self, book_uid: str, session: AsyncSession):
        book_to_delete = await self.get_book_by_uid(book_uid, session)
        if book_to_delete is not None:
            await session.delete(book_to_delete)
            await session.commit()
            return True
        else:
            return False