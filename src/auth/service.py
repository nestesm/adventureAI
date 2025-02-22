from sqlalchemy import select
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_session
from .schemas import UserCreate, UserDB
from .models import UserModel
from .utils import password_manager

class UserService:
    @classmethod
    async def add_user(cls, session: AsyncSession, user: UserCreate) -> UserModel:
            query = select(UserModel).where(UserModel.email == user.email)
            result = await session.execute(query)
            existing_user = result.scalar_one_or_none()
            if existing_user:
                    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with this email already exist.")
            
            hashed_password = password_manager.get_hashed_password(user.password)

            db_user = UserModel(
                    email=user.email,
                    name=user.name,
                    hashed_password=hashed_password,
                    is_active=True,
                    is_superuser=False,
                    is_verified=False
            )

            session.add(db_user)
            await session.commit()
            await session.refresh(db_user)

            return db_user
    
    @classmethod
    async def get_user(cls, session: AsyncSession, user):
         pass 


class AuthService:
    @classmethod
    async def authenticate_user(email: str, password: str):
         pass
