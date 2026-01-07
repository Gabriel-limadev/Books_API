from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List

from app.db.session import get_session
from app.services.stats_service import StatsService
from app.schemas.stats import StatsOverview, StatsCategories

router = APIRouter()
service = StatsService()

### Rota de stats
@router.get('/overview', response_model=StatsOverview)
def get_all_books(session: Session = Depends(get_session)):
    '''
    Lista todos as informações sobre as estatisticas dos livros
    ---
    responses: 200
    Exemplo de chamada: /api/v1/stats/overview
    '''
    return service.list_stats_overview(session)

@router.get('/categories', response_model=List[StatsCategories])
def get_all_books(session: Session = Depends(get_session)):
    '''
    Lista todos as informações sobre as estatisticas das categorias
    ---
    responses: 200
    Exemplo de chamada: /api/v1/stats/categories
    '''
    return service.list_stats_categories(session)
