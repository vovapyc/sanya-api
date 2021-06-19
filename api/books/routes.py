from typing import List

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from api import deps
from .crud import book_crud
from .schemas import *

router = APIRouter()


@router.get('/', response_model=List[Book])
def get_all_books(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> List[Book]:
    return book_crud.get_multi(db, skip=skip, limit=limit)


@router.get('/{book_id}', response_model=Book)
def get_one_book(
        book_id: int,
        db: Session = Depends(deps.get_db),
) -> Book:
    book = book_crud.get(db=db, id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put('/{book_id}', response_model=Book)
def update_book(
        book_id: int,
        book_in: UpdateBook,
        db: Session = Depends(deps.get_db),
) -> Book:
    book = book_crud.get(db=db, id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book = book_crud.update(db, db_obj=book, obj_in=book_in)
    return book


@router.delete('/{book_id}', status_code=status.HTTP_200_OK)
def delete_book(
        book_id: int,
        db: Session = Depends(deps.get_db),
):
    book = book_crud.get(db=db, id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book_crud.remove(db=db, id=book_id)


@router.post('/', response_model=Book)
def create_book(
        book: CreateBook,
        db: Session = Depends(deps.get_db),
) -> Book:
    book = book_crud.create(db, obj_in=book)
    return book
