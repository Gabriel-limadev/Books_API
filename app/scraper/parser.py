import pandas as pd
import sqlite3

from book_scraper import BookScraper


# Instancia o scraper responsável por coletar os dados dos livros
scraper = BookScraper()

try:
    # Executa o scraping completo e retorna uma as informações de todos os livros    
    books_data = scraper.scrape_all_books()

finally:
    scraper.close()


# Converte a lista de dicionários em um DataFrame do pandas
df = pd.DataFrame(books_data)


# Cria uma conexão com o banco de dados SQLite
conn = sqlite3.connect("db/books.db")

# Salva o DataFrame na tabela "books"
df.to_sql("books", conn, if_exists="replace", index=False)

# Fecha a conexão com o banco de dados
conn.close()