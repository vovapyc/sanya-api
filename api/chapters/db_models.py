from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base_models import Base


class Chapter(Base):
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)

    title = Column(String(50))
    original = Column(String)
    translation = Column(String)

    book_id = Column(Integer, ForeignKey('book.id'))
    book = relationship('Book', back_populates='chapters')

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
