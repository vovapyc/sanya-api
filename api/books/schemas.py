from pydantic import BaseModel


class BaseBook(BaseModel):
    title: str
    published: bool = False
    description: str
    author: str


class CreateBook(BaseBook):
    pass


class UpdateBook(BaseBook):
    pass


class Book(BaseBook):
    id: int

    class Config:
        orm_mode = True
