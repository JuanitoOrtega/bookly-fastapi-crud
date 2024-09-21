from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.books.routes import book_router
from src.auth.routes import auth_router
from src.db.main import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print(f'Server is starting...')
    await init_db()
    yield
    print(f'Server has been stopped...')


version = 'v1'

app = FastAPI(
    title='Bookly API',
    description='A simple REST API to manage book reviews service',
    version=version,
    lifespan=life_span
)


app.include_router(book_router, prefix=f'/api/{version}/books', tags=['Books'])
app.include_router(auth_router, prefix=f'/api/{version}/users', tags=['Users'])