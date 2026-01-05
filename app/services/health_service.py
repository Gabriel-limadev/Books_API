from fastapi import HTTPException
from sqlmodel import Session, select

class HealthService:
    def check_health(
            self, 
            session: Session
        ) -> dict: 
        try:
            session.exec(select(1)).first()
            return {
                'status': 'OK',
                'database': 'connected'
            }
        except Exception:
            raise HTTPException(status_code=500, detail='Database connection failed')
 