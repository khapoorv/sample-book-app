
from datetime import datetime
from pydantic import BaseModel, Field
from .base import BaseEntity

class Loan(BaseEntity):
    user_id: str
    book_id: str
    loan_date: datetime = Field(default_factory=datetime.utcnow)
    due_date: datetime
    return_date: datetime | None = None
