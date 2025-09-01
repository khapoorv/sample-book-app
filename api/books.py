
from fastapi import APIRouter, Depends, HTTPException, status
from ..services.book_service import BookService
from ..services.loan_service import LoanService
from ..services.reservation_service import ReservationService
from ..schemas.book import BookInDB
from ..schemas.loan import LoanInDB
from ..models.user import User
from ..auth.security import get_current_active_user
from ..utils.exceptions import BookNotFoundException, BookNotAvailableException, LoanAlreadyExistsException

router = APIRouter()
book_service = BookService()
loan_service = LoanService(book_service)
reservation_service = ReservationService(book_service)

@router.get("/", response_model=list[BookInDB])
def get_all_books():
    return book_service.get_all_books()

@router.get("/{book_id}", response_model=BookInDB)
def get_book(book_id: str):
    try:
        return book_service.get_book_by_id(book_id)
    except BookNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.post("/{book_id}/borrow", response_model=LoanInDB)
def borrow_book(book_id: str, current_user: User = Depends(get_current_active_user)):
    try:
        return loan_service.borrow_book(current_user.id, book_id)
    except (BookNotFoundException, BookNotAvailableException, LoanAlreadyExistsException) as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/{book_id}/return", response_model=LoanInDB)
def return_book(book_id: str, current_user: User = Depends(get_current_active_user)):
    try:
        return loan_service.return_book(current_user.id, book_id)
    except BookNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/{book_id}/reserve")
def reserve_book(book_id: str, current_user: User = Depends(get_current_active_user)):
    try:
        reservation = reservation_service.create_reservation(current_user.id, book_id)
        return {"message": "Reservation created successfully", "reservation_id": reservation.id}
    except (BookNotFoundException, BookNotAvailableException, ValueError) as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
