from .models import User
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .schemas import UserCreateModel
from .utils import generate_passwd_hash


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_by_email(self, email: str) -> User:
        statement = select(User).where(User.email == email)
        result = await self.session.exec(statement)
        user = result.first()
        return user
    
    async def user_exists(self, email: str) -> bool:
        user = await self.get_user_by_email(email, self.session)
        return True if user is not None else False

    async def create_user(self, user_data: UserCreateModel) -> User:
        user_data_dict = user_data.model_dump()
        new_user = User(**user_data_dict)
        new_user.password_hash = generate_passwd_hash(user_data_dict["password"])
        self.session.add(new_user)
        await self.session.commit()
        return new_user

    async def update_user(self, user: User, user_data: dict) -> User:
        for key, value in user_data.items():
            setattr(user, key, value)
        await self.session.commit()
        return user

    async def delete_user(self, user: User):
        self.session.delete(user)
        await self.session.commit()