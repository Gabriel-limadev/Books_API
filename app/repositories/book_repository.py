from sqlmodel import Session, select
from app.models.book import Book

class BookRepository:
    
    # Metodo para capturar todos os livros
    def get_all_books(
            self,
            session: Session
        ) -> list[Book]:
        
        statement = select(Book)
        return session.exec(statement).all()
    
    # Metodo para capturar livro de acordo com id
    def get_book_by_id(
            self,
            session: Session, 
            book_id: int
        ) -> Book:
        
        statement = select(Book).where(Book.id == book_id)
        return session.exec(statement).first()
    
    # Metodo para capturar livros de acordo com filtro de titulo, categoria, ou os dois
    def get_book_by_title_or_category(
            self,
            session: Session, 
            book_title: str | None = None, 
            book_category: str | None = None
        ) -> list[Book]:

        # Caso o title não seja passado, se filtra apenas pela categoria
        if not book_title and book_category:
            statement = select(Book).where(Book.category == book_category)
        
        # Caso a category não seja passada, se filtra apenas pelo title
        elif not book_category and book_title:
            statement= select(Book).where(Book.title.ilike(f"%{book_title}%"))
        else:
        # Se não filtramos pelos dois
            statement = select(Book).where(Book.title.ilike(f"%{book_title}%")).where(Book.category == book_category)
        
        # Retorna todo o resultado
        return session.exec(statement).all()
    
    # Metodo para capturar todas as categorias
    def get_all_categories(
            self,
            session: Session
        ) -> list[str]:
        statement = select(Book.category).distinct()
        return session.exec(statement).all()