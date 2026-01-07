from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List

from app.db.session import get_session
from app.services.book_service import BookService
from app.schemas.book import BookResponse

router = APIRouter()
service = BookService()

### Rota de livros
@router.get('/', response_model=List[BookResponse])
def get_all_books(session: Session = Depends(get_session)):
    '''
    Lista todos as informações sobre os livros
    ---
    responses: 200
    Exemplo de chamada: /api/v1/books 
    '''
    return service.list_all_books(session)

@router.get('/search', response_model=List[BookResponse])
def get_book_by_title_or_category(title: str | None = None, category: str | None = None, session: Session = Depends(get_session)):
    '''
    Lista livros com filtro de titulo e/ou categoria 
    ---
    responses: 200
    Exemplo de chamada: /api/v1/books/search?title=harry
    '''
    return service.list_books_by_title_or_category(session, title, category)

@router.get('/top-rated', response_model=List[BookResponse])
def get_book_top_rated(top_n: int | None = None, session: Session = Depends(get_session)):
    '''
    Lista livros com maiores ratings 
    ---
    responses: 200
    Exemplo de chamada: /api/v1/books/top-rated?top_n=5
    '''
    return service.list_books_top_rated(session, top_n)

@router.get('/price-range', response_model=List[BookResponse])
def get_book_by_price_range(min: float, max: float, session: Session = Depends(get_session)):
    '''
    Lista livros de acordo com o range de preços passado
    ---
    responses: 200
    Exemplo de chamada: /api/v1/books/price-range?min=2&max=10
    '''
    return service.list_books_by_price_range(session, min, max)

@router.get('/{id}', response_model=BookResponse)
def get_book_by_id(id: int, session: Session = Depends(get_session)):
    '''
    Lista livro de acordo com id
    ---
    responses: 200
    Exemplo de chamada: /api/v1/books/1 
    '''
    return service.list_book_by_id(session, id)