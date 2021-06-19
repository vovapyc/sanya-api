from helpers.base_crud import CRUDBase
from .db_models import Book
from .schemas import CreateBook, UpdateBook


class CRUDBook(CRUDBase[Book, CreateBook, UpdateBook]):
    pass


book_crud = CRUDBook(Book)
