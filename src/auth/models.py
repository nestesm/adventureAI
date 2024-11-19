import uuid
from sqlalchemy import TIMESTAMP, JSON
from sqlalchemy.orm import Mapped, mapped_column, validates
from sqlalchemy.dialects.postgresql import UUID
from enum import Enum

from database import Base, metadata


class UserModel(Base):
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=True)
    is_verified: Mapped[bool] = mapped_column(nullable=False)
    is_superuser: Mapped[bool] = mapped_column(nullable=False)
    
    
    @validates('email')
    def validate_email(self, key, address):
        if '@' not in address:
            raise ValueError('failed simple email validation')
        return address