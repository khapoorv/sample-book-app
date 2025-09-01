
from datetime import datetime
from pydantic import BaseModel

class LoanBase(BaseModel):
    book_id: str

class LoanCreate(LoanBase):
    user_id: str

class LoanInDB(LoanBase):
    id: str
    user_id: str
    loan_date: datetime
    due_date: datetime
    return_date: datetime | None = None

    class Config:
        orm_mode = True
