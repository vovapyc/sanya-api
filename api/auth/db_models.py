from datetime import datetime

from sqlalchemy import Column, String, DateTime

from db.base_models import Base


class User(Base):
    id = Column(String, primary_key=True, unique=True)

    username = Column(String, unique=True)
    password = Column(String)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
