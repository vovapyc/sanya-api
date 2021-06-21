from datetime import datetime

from sqlalchemy import Column, String, DateTime, Integer

from db.base_models import Base


class User(Base):
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)

    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
