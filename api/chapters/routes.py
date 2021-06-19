from typing import List

from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from api import deps
from api.books.crud import book_crud
from .crud import chapter_crud
from .schemas import *

router = APIRouter()


@router.post('/{book_id}/chapters', response_model=Chapter)
def create_chapter(
        book_id: int,
        chapter_in: CreateChapter,
        db: Session = Depends(deps.get_db),
):
    book = book_crud.get(db=db, id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    chapter_in = CreateChapterInDb(**jsonable_encoder(chapter_in), book_id=book_id)
    chapter = chapter_crud.create(db, obj_in=chapter_in)
    return chapter


@router.get('/{book_id}/chapters', response_model=List[Chapter])
def get_chapters_by_book(
        book_id: int,
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> List[Chapter]:
    book = book_crud.get(db=db, id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    chapters = chapter_crud.get_by_book_id(db, book_id, skip=skip, limit=limit)

    return chapters


@router.get('/{book_id}/chapters/{chapter_id}', response_model=Chapter)
def update_chapter(
        book_id: int,
        chapter_id: int,
        chapter_in: UpdateChapter,
        db: Session = Depends(deps.get_db),
) -> List[Chapter]:
    chapter = chapter_crud.get(db=db, id=chapter_id)
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    if chapter.book_id != book_id:
        raise HTTPException(status_code=400, detail="Book ID is wrong")

    chapter = chapter_crud.update(db, db_obj=chapter, obj_in=chapter_in)
    return chapter


@router.delete('/{book_id}/chapters/{chapter_id}', status_code=status.HTTP_200_OK)
def delete_chapter(
        book_id: int,
        chapter_id: int,
        db: Session = Depends(deps.get_db),
):
    chapter = chapter_crud.get(db=db, id=chapter_id)
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    if chapter.book_id != book_id:
        raise HTTPException(status_code=400, detail="Book ID is wrong")

    chapter_crud.remove(db, id=chapter_id)
