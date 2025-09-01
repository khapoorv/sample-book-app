
from pydantic import BaseModel, Field
from .base import BaseEntity

class Book(BaseEntity):
    title: str
    author: str
    isbn: str
    genre: str
    publication_year: int
    total_copies: int = Field(..., gt=0)
    available_copies: int
