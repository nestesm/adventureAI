from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator
from sqlalchemy import MetaData

from config import settings


Base: DeclarativeMeta = declarative_base()
metadata = MetaData()

engine = create_async_engine(
    settings.DATABASE_URL_async,
    echo=True,
    pool_size=10,
    max_overflow=20,
)

async_session_maker = sessionmaker(engine, class_=AsyncSession) 

async def get_async_session()-> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session