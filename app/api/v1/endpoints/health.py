from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db.session import get_session
from app.services.health_service import HealthService

router = APIRouter()
service = HealthService()

@router.get('/')
def health_check(session: Session = Depends(get_session)):
    return service.check_health(session)
