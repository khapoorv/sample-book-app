
from datetime import datetime, timedelta
from ..db.database import DB
from ..models.loan import Loan
from ..services.book_service import BookService
from ..utils.exceptions import BookNotAvailableException, LoanAlreadyExistsException, BookNotFoundException

class LoanService:
    def __init__(self, book_service: BookService):
        self.book_service = book_service

    def borrow_book(self, user_id: str, book_id: str) -> Loan:
        book = self.book_service.get_book_by_id(book_id)
        if book.available_copies < 1:
            raise BookNotAvailableException("No available copies of this book to borrow.")

        for loan in DB['loans'].values():
            if loan['user_id'] == user_id and loan['book_id'] == book_id and loan['return_date'] is None:
                raise LoanAlreadyExistsException("User has already borrowed this book.")

        book.available_copies -= 1
        DB["books"][book.id] = book.dict()

        loan = Loan(
            user_id=user_id,
            book_id=book_id,
            due_date=datetime.utcnow() + timedelta(days=14)
        )
        DB["loans"][loan.id] = loan.dict()
        return loan

    def return_book(self, user_id: str, book_id: str) -> Loan:
        loan_id_to_return = None
        for loan_id, loan_data in DB['loans'].items():
            if loan_data['user_id'] == user_id and loan_data['book_id'] == book_id and loan_data['return_date'] is None:
                loan_id_to_return = loan_id
                break

        if not loan_id_to_return:
            raise BookNotFoundException("No active loan found for this book by the user.")

        loan = Loan(**DB['loans'][loan_id_to_return])
        loan.return_date = datetime.utcnow()
        DB['loans'][loan_id_to_return] = loan.dict()

        book = self.book_service.get_book_by_id(book_id)
        book.available_copies += 1
        DB["books"][book.id] = book.dict()

        return loan
