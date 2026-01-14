from sqlmodel import Session
from app.scraper.book_scraper import BookScraper
from app.scraper.parser import parse_books
from app.models.book import Book


class ScrapingService:
    def __init__(self, db: Session):
        self.db = db

    def run(self):
        scraper = BookScraper()

        try:
            books_data = scraper.scrape_all_books()
        finally:
            scraper.close()

        df = parse_books(books_data)

        inserted = 0
        updated = 0

        for _, row in df.iterrows():
            book = self.db.query(Book).filter(
                Book.id == row["id"]
            ).first()

            if book:
                book.price = row["price"]
                book.rating = row["rating"]
                book.category = row["category"]
                book.availability = row["availability"]
                updated += 1
            else:
                self.db.add(Book(
                    title=row["title"],
                    price=row["price"],
                    rating=row["rating"],
                    category=row["category"],
                    availability=row["availability"]
                ))
                inserted += 1

        self.db.commit()

        return {
            "total": len(df),
            "inserted": inserted,
            "updated": updated
        }
