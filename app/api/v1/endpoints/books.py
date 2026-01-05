from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List

from app.db.session import get_session
from app.services.book_service import BookService
from app.schemas.book import BookResponse

router = APIRouter()
service = BookService()

@router.get('/', response_model=List[BookResponse])
def get_all_books(session: Session = Depends(get_session)):
    return service.list_all_books(session)

@router.get('/books/search', response_model=List[BookResponse])
def get_book_by_title_or_category(title: str | None = None, category: str | None = None, session: Session = Depends(get_session)):
    return service.list_books_by_title_or_category(session, title, category)

@router.get('/books/{id}', response_model=BookResponse)
def get_book_by_id(id: int, session: Session = Depends(get_session)):
    return service.list_book_by_id(session, id)