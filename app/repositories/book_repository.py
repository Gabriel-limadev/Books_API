from sqlmodel import Session, select, func
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
    
    # Metodo para listar os livros com as melhores avaliações
    def get_top_rated(
            self, 
            session: Session,
            top_n: int | None = None
    ) -> list[Book]:
        
        statement = select(Book).order_by(Book.rating.desc())
        
        # Caso seja passado o limite desejado
        if top_n is not None:
            statement = statement.limit(top_n)

        return session.exec(statement).all()
    
    # Metodo para listar os livros filtrados de acordo com um range de preço
    def get_book_by_price_range(
            self, 
            session: Session,
            min_price: float,
            max_price: float
    ) -> list[Book]:
        statement = select(Book).where(Book.price >= min_price).where(Book.price <= max_price)
        return session.exec(statement).all()

    # Metodo para capturar todas as categorias
    def get_all_categories(
            self,
            session: Session
        ) -> list[str]:
        statement = select(Book.category).distinct()
        return session.exec(statement).all()
    
    # Metodo para capturar as estatisticas gerais dos livros
    def get_stats_overview(
            self,
            session: Session
        ) -> list[dict]:
        books_stmt = select(func.count(Book.id).label('total_livros'), func.avg(Book.price).label('preco_medio'))
        total_livros, preco_medio = session.exec(books_stmt).one()
        ratings_distribuition = select(Book.rating, func.count(Book.rating).label('quantidade')).group_by(Book.rating).order_by(Book.rating)
        ratings_result = session.exec(ratings_distribuition).all()

        return {
            'total_livros': total_livros,
            'preco_medio': float(preco_medio) if preco_medio else 0.0,
            'distribuicao_ratings': [
                {
                    'rating': rating,
                    'quantidade': quantidade
                }
                for rating, quantidade in ratings_result
            ]
        }
            
    # Metodo para capturar as estatisticas gerais dos livros detalhadas pelas categorias
    def get_stats_categories(
            self,
            session: Session
        ) -> list[dict]:
        statement = select(
                            Book.category, 
                            func.count(Book.id).label('total_livros'),
                            func.avg(Book.price).label('preco_medio')
                          ).group_by(Book.category)
        result = session.exec(statement).all()
        return [
            {
                'category': category,
                'total_livros': total_livros,
                'preco_medio': float(preco_medio) if preco_medio else 0.0
            }
            for category, total_livros, preco_medio in result
        ]