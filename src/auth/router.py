from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserCreate, User
from .service import UserService
from core.database import get_async_session

user_router = APIRouter(
    prefix = "/users",
    tags = ["user"]
)

auth_router = APIRouter(
    prefix = "/auth",
    tags = ["auth"]
)

@user_router.post("/register")
async def add_user(
    new_user: UserCreate,
    session: AsyncSession = Depends(get_async_session)
) -> User:
    return await UserService.add_user(session, new_user)
