
from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    isbn: str
    genre: str
    publication_year: int

class BookCreate(BookBase):
    total_copies: int

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    isbn: str | None = None
    genre: str | None = None
    publication_year: int | None = None
    total_copies: int | None = None

class BookInDB(BookBase):
    id: str
    total_copies: int
    available_copies: int

    class Config:
        orm_mode = True
