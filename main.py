import uvicorn
from fastapi import FastAPI

from api.books.routes import router as books_router
from api.chapters.routes import router as chapters_router
from db.init_db import init_db
from db.session import SessionLocal

app = FastAPI()

app.include_router(books_router, prefix='/books')
app.include_router(chapters_router, prefix='/books')

if __name__ == '__main__':
    db = SessionLocal()
    init_db(db)

    uvicorn.run(app, host='0.0.0.0')
