from sqlalchemy import Column, Integer, DateTime, func
from settings.db import Base


class DefaultModel(Base):
    """Абстрактная модель"""
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    created_at = Column(DateTime, server_default=func.now())
