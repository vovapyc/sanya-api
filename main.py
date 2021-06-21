import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.auth.routes import router as auth_router
from api.books.routes import router as books_router
from api.chapters.routes import router as chapters_router
from db.init_db import init_db
from db.session import SessionLocal

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books_router, prefix='/books')
app.include_router(chapters_router, prefix='/books')
app.include_router(auth_router, prefix='/auth')

if __name__ == '__main__':
    db = SessionLocal()
    init_db(db)

    uvicorn.run(app, host='0.0.0.0')
