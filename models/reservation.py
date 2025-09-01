
from datetime import datetime
from pydantic import BaseModel, Field
from .base import BaseEntity

class Reservation(BaseEntity):
    user_id: str
    book_id: str
    reservation_date: datetime = Field(default_factory=datetime.utcnow)
