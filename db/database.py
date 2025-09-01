
from datetime import datetime, timedelta

# In-memory storage for the library entities
# In a real-world application, this would be a database like PostgreSQL, MySQL, etc.

DB = {
    "books": {
        "1": {
            "id": "1",
            "title": "The Hitchhiker's Guide to the Galaxy",
            "author": "Douglas Adams",
            "isbn": "978-0345391803",
            "genre": "Science Fiction",
            "publication_year": 1979,
            "total_copies": 5,
            "available_copies": 5
        },
        "2": {
            "id": "2",
            "title": "Pride and Prejudice",
            "author": "Jane Austen",
            "isbn": "978-0141439518",
            "genre": "Romance",
            "publication_year": 1813,
            "total_copies": 3,
            "available_copies": 1
        },
        "3": {
            "id": "3",
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "isbn": "978-0061120084",
            "genre": "Classic",
            "publication_year": 1960,
            "total_copies": 4,
            "available_copies": 0
        }
    },
    "users": {},
    "loans": {
        "1": {
            "id": "1",
            "user_id": "some_user_id_placeholder", # Will be replaced when users are created
            "book_id": "2",
            "loan_date": datetime.utcnow() - timedelta(days=10),
            "due_date": datetime.utcnow() + timedelta(days=4),
            "return_date": None
        }
    },
    "reservations": {},
    "fines": {}
}
