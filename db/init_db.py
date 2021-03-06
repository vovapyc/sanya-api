from sqlalchemy.orm import Session

from api.auth.db_models import User  # noqa: F401
from api.books.db_models import Book  # noqa: F401
from .base_models import Base
from .session import engine


def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)
