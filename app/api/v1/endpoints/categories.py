from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List

from app.db.session import get_session
from app.services.book_service import BookService

router = APIRouter()
service = BookService()

@router.get('/', response_model=List[str])
def get_all_categories(session: Session = Depends(get_session)):
    return service.list_all_categories(session)
