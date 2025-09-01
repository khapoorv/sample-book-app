
from ..db.database import DB
from ..models.reservation import Reservation
from ..services.book_service import BookService
from ..utils.exceptions import BookNotAvailableException, BookNotFoundException

class ReservationService:
    def __init__(self, book_service: BookService):
        self.book_service = book_service

    def create_reservation(self, user_id: str, book_id: str) -> Reservation:
        book = self.book_service.get_book_by_id(book_id)
        if book.available_copies > 0:
            raise BookNotAvailableException("Book is available for borrowing, no need for reservation.")

        for r in DB['reservations'].values():
            if r['user_id'] == user_id and r['book_id'] == book_id:
                raise ValueError("User has already reserved this book.")

        reservation = Reservation(user_id=user_id, book_id=book_id)
        DB["reservations"][reservation.id] = reservation.dict()
        return reservation

    def get_reservations_for_book(self, book_id: str) -> list[Reservation]:
        return [Reservation(**r) for r in DB['reservations'].values() if r['book_id'] == book_id]

    def notify_next_in_line(self, book_id: str):
        reservations = sorted(
            self.get_reservations_for_book(book_id),
            key=lambda r: r.reservation_date
        )
        if reservations:
            next_user_reservation = reservations[0]
            # In a real app, you would send an email or notification.
            print(f"Notification: Book {book_id} is available for user {next_user_reservation.user_id}")
            # You might want to remove the reservation after notification
            # or implement a time limit for the user to borrow the book.
            del DB['reservations'][next_user_reservation.id]
