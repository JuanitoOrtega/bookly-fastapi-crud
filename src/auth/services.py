from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from .models import User
from .schemas import UserCreateRequestl
from .utils import generate_passwd_hash


class UserService:
    async def get_user_by_email(self, email: str, session: AsyncSession) -> User:
        statement = select(User).where(User.email == email)
        result = await session.exec(statement)
        user = result.first()
        return user
    
    async def user_exists(self, email: str, session: AsyncSession) -> bool:
        user = await self.get_user_by_email(email, session)
        return True if user is not None else False

    async def create_user(self, user_data: UserCreateRequestl, session: AsyncSession) -> User:
        user_data_dict = user_data.model_dump()
        new_user = User(**user_data_dict)
        
        new_user.password_hash = generate_passwd_hash(user_data_dict["password"])
        session.add(new_user)
        await session.commit()
        return new_user

    async def update_user(self, user: User, user_data: dict, session: AsyncSession) -> User:
        for key, value in user_data.items():
            setattr(user, key, value)
        await session.commit()
        return user

    async def delete_user(self, user: User, session: AsyncSession):
        session.delete(user)
        await session.commit()