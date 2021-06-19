from pydantic import BaseModel


class BaseChapter(BaseModel):
    title: str
    original: str
    translation: str


class CreateChapter(BaseChapter):
    pass


class CreateChapterInDb(BaseChapter):
    book_id: int


class Chapter(BaseChapter):
    id: int

    class Config:
        orm_mode = True


class UpdateChapter(BaseChapter):
    pass
