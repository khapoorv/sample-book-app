
from fastapi import APIRouter, Depends, HTTPException, status
from ..services.book_service import BookService
from ..schemas.book import BookCreate, BookUpdate, BookInDB
from ..models.user import User, UserRole
from ..auth.security import get_current_active_user
from ..utils.exceptions import BookNotFoundException, NotAnAdminException

router = APIRouter()
book_service = BookService()

def get_admin_user(current_user: User = Depends(get_current_active_user)) -> User:
    if current_user.role != UserRole.LIBRARIAN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user does not have permissions to perform this action."
        )
    return current_user

@router.post("/books", response_model=BookInDB, status_code=status.HTTP_201_CREATED)
def create_book(book_create: BookCreate, admin: User = Depends(get_admin_user)):
    return book_service.create_book(book_create)

@router.put("/books/{book_id}", response_model=BookInDB)
def update_book(book_id: str, book_update: BookUpdate, admin: User = Depends(get_admin_user)):
    try:
        return book_service.update_book(book_id, book_update)
    except BookNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: str, admin: User = Depends(get_admin_user)):
    try:
        book_service.delete_book(book_id)
    except BookNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
