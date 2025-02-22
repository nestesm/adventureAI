import uuid
from sqlalchemy.orm import Mapped, mapped_column, validates
from sqlalchemy.dialects.postgresql import UUID

from core.database import Base


class UserModel(Base):
    __tablename__ = 'users'
    
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=True)
    is_verified: Mapped[bool] = mapped_column(nullable=False)
    is_superuser: Mapped[bool] = mapped_column(nullable=False)
    
    
    @validates('email')
    def validate_email(self, key, address):
        if '@' not in address:
            raise ValueError('failed simple email validation')
        return address