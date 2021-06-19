from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from api.chapters.db_models import Chapter

from db.base_models import Base


class Book(Base):
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)

    title = Column(String(50))
    published = Column(Boolean, default=False)
    description = Column(String)
    author = Column(String(50))

    chapters = relationship(Chapter, back_populates='book')

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
