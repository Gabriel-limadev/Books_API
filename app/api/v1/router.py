from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from app.api.v1.endpoints import books, categories, health, stats, auth, scraping

# Routers separados
public_router = APIRouter()
private_router = APIRouter(
    dependencies=[Depends(get_current_user)]
)

# Rotas públicas
public_router.include_router(auth.router, prefix='/auth', tags=['Auth'])
public_router.include_router(health.router, prefix='/health', tags=['Health'])
public_router.include_router(books.router, prefix='/books', tags=['Books'])
public_router.include_router(categories.router, prefix='/categories', tags=['Categories'])
public_router.include_router(stats.router, prefix='/stats', tags=['Stats'])

# Rotas privadas
private_router.include_router(scraping.router, prefix='/scraping', tags=['Scraping'])

# Router principal
router = APIRouter()
router.include_router(public_router)
router.include_router(private_router)