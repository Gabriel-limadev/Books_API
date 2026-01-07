from fastapi import HTTPException
from sqlmodel import Session
from app.models.book import Book
from app.repositories.book_repository import BookRepository

class BookService:
    def __init__(self):
        self.repository = BookRepository()

    def list_all_books(
            self, 
            session: Session
        ) -> list[Book]: 
        '''
        Retorna uma lista com todos os livros
        '''
        return self.repository.get_all_books(session)
    
    def list_book_by_id(
            self, 
            session: Session, 
            book_id: int
        ) -> Book: 
        ''' 
        Retorna apenas um livro de acordo com o id passado
        '''
        book = self.repository.get_book_by_id(session, book_id)

        # Caso não seja achado nenhum livro, é retornado um erro.
        if not book: 
            raise HTTPException(status_code=404, detail='Book not found!')
        return book
    
    def list_books_by_title_or_category(
            self, 
            session: Session, 
            book_title: str | None = None, # Valor padrão None caso não seja passado esse parametro na url 
            book_category: str | None = None # Valor padrão None caso não seja passado esse parametro na url
        ) -> list[Book]: 
        ''' 
        Retorna uma lista com um ou mais livros de acordo com o filtro
        ''' 
        # É necessario que contenha pelo menos um filtro, se não retornará uma mensagem de erro.
        if not book_title and not book_category:
            raise HTTPException(status_code=400, detail = 'You must inform title or category!')
        
        # Busca livros de acordo com o title e category passados
        books = self.repository.get_book_by_title_or_category(session, book_title, book_category)

        # Caso não aja resultado de livros será retornado um erro.
        if not books:
            raise HTTPException(status_code = 404, detail='No books found!')

        return books
    
    def list_books_top_rated(
            self,
            session: Session,
            top_n: int | None = None # Valor padrão None caso não seja passado esse parametro na url 
        ) -> list[Book]:
        '''
        Retorna os livros com maiores ratings
        Pode ser passado como parametro o numero de livros desejados
        '''
        books = self.repository.get_top_rated(session, top_n)
        return books
    
    def list_books_by_price_range(
            self,
            session: Session, 
            min_price: float, 
            max_price: float
        ) -> list[Book]:
        '''
        Retorna os livros filtrados com um range de preços
        '''
        if min_price > max_price:
            raise HTTPException(
                status_code=400,
                detail='min_price cannot be greater than max_price'
            )
            
        books = self.repository.get_book_by_price_range(session, min_price, max_price)
        return books
    
    def list_all_categories(
            self,
            session: Session
    ) -> list[str]:
        '''
        Retorna todas as categorias existentes
        '''
        categories = self.repository.get_all_categories(session)
        return categories