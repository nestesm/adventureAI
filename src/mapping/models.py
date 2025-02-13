import uuid
from datetime import datetime
from sqlalchemy import func, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2 import Geometry
from sqlalchemy.dialects.postgresql import JSON

from core.database import Base


class TrajectoryModel(Base):
    __tablename__ = 'trajectory'
    
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    start_marker: Mapped[Geometry] = mapped_column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    end_marker: Mapped[Geometry] = mapped_column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    total_time: Mapped[int] = mapped_column(nullable=False)
    distance: Mapped[int] = mapped_column(nullable=False)
    preferences: Mapped[JSON] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
    
    user_id: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('users.id', ondelete='CASCADE'))


class LocationModel(Base):
    __tablename__ = 'location'
    
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()
    marker: Mapped[Geometry] = mapped_column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    arrival_time: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))
    stay_duration: Mapped[int] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
    
    
    trajectory_id: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('trajectory.id', ondelete='CASCADE'))
    