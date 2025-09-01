
from ..db.database import DB
from ..models.book import Book
from ..schemas.book import BookCreate, BookUpdate
from ..utils.exceptions import BookNotFoundException

class BookService:

    def get_book_by_id(self, book_id: str) -> Book:
        book_data = DB["books"].get(book_id)
        if not book_data:
            raise BookNotFoundException(f"Book with id {book_id} not found")
        return Book(**book_data)

    def get_all_books(self) -> list[Book]:
        return [Book(**book_data) for book_data in DB["books"].values()]

    def create_book(self, book_create: BookCreate) -> Book:
        book = Book(
            title=book_create.title,
            author=book_create.author,
            isbn=book_create.isbn,
            genre=book_create.genre,
            publication_year=book_create.publication_year,
            total_copies=book_create.total_copies,
            available_copies=book_create.total_copies
        )
        DB["books"][book.id] = book.dict()
        return book

    def update_book(self, book_id: str, book_update: BookUpdate) -> Book:
        book = self.get_book_by_id(book_id)
        update_data = book_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(book, key, value)
        DB["books"][book_id] = book.dict()
        return book

    def delete_book(self, book_id: str):
        if book_id not in DB["books"]:
            raise BookNotFoundException(f"Book with id {book_id} not found")
        del DB["books"][book_id]
