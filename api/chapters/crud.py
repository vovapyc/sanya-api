from typing import Any, List

from sqlalchemy.orm import Session

from helpers.base_crud import CRUDBase
from .db_models import Chapter
from .schemas import CreateChapter, UpdateChapter


class CRUDChapter(CRUDBase[Chapter, CreateChapter, UpdateChapter]):
    def get_by_book_id(self, db: Session, book_id: Any, *, skip: int = 0, limit: int = 100) -> List[Chapter]:
        return db.query(self.model).filter(self.model.book_id == book_id).offset(skip).limit(limit).all()


chapter_crud = CRUDChapter(Chapter)
