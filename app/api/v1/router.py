from fastapi import APIRouter
from app.api.v1.endpoints import books, categories, health

router = APIRouter()
router.include_router(books.router, prefix='/books', tags=['Books'])
router.include_router(categories.router, prefix='/categories', tags=['Categories'])
router.include_router(health.router, prefix='/health', tags=['Health'])