import uuid
from pydantic import Field, BaseModel

class UserBase(BaseModel):
    email: str | None = Field(None)
    name: str | None = Field(None, description="full name")
    is_active: bool = Field(True)
    is_verified: bool = Field(False)
    is_superuser: bool = Field(False)

    class Config:
        from_attributes = True

class User(UserBase):
    id: uuid.UUID
    email: str
    name: str
    is_active: bool
    is_verified: bool 
    is_superuser: bool 

class UserCreate(UserBase):
    email: str
    name: str
    password: str

# class UserUpdate(UserBase):
#     password: str


class UserDB(UserBase):
    hashed_password: str 