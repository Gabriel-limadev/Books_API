from sqlmodel import Session
from app.repositories.book_repository import BookRepository

class StatsService:
    def __init__(self):
        self.repository = BookRepository()

    def list_stats_overview(
            self,
            session: Session
    ) -> list[dict]:
        '''
        Retorna todas as estatisticas relacionadas aos livros
        '''
        stats_books = self.repository.get_stats_overview(session)
        return stats_books
    
    def list_stats_categories(
            self,
            session: Session
    ) -> list[dict]:
        '''
        Retorna todas as estatisticas relacionadas aos livros detalhadas por categoria
        '''
        stats_categories = self.repository.get_stats_categories(session)
        return stats_categories
