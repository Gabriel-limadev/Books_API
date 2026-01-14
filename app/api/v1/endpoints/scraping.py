from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session
from app.services.scraping_service import ScrapingService

router = APIRouter()

@router.post("/")
def scrape_books(session: Session = Depends(get_session)):
    service = ScrapingService(session)
    return service.run()
