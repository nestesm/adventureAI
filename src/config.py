from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import find_dotenv
import os


class Settings(BaseSettings):
    DATABASE_HOST: str = os.getenv(validation_alias="DATABASE_HOST")
    DATABASE_PORT: str = os.getenv(validation_alias="DATABASE_PORT")
    DATABASE_USER: str = os.getenv(validation_alias="DATABASE_USER")
    DATABASE_PASSWORD: str = os.getenv(validation_alias="DATABASE_PASSWORD")
    DATABASE_NAME: str = os.getenv(validation_alias="DATABASE_NAME")
    SECRET_JWT: str = os.getenv(validation_alias="SECRET_JWT")
    SECRET_PASS: str = os.getenv(validation_alias="SECRET_PASS")
    SMTP_PASSWORD: str = os.getenv(validation_alias="SMTP_PASSWORD")
    REDIS_PASSWORD: str = os.getenv(validation_alias="REDIS_PASSWORD")
    REDIS_USER: str = os.getenv(validation_alias="REDIS_USER")
    REDIS_USER_PASSWORD: str = os.getenv(validation_alias="REDIS_USER_PASSWORD")
    
    @property
    def DATABASE_URL_async(self) -> str:
        return f"postgresql+asyncpg://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"
    
    class Config:
        env_file = find_dotenv(usecwd=True)
        case_sensitive=True

   
settings = Settings() 
DATABASE_URL: str = f"postgresql+asyncpg://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"