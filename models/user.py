
from pydantic import BaseModel, EmailStr
from enum import Enum
from .base import BaseEntity

class UserRole(str, Enum):
    MEMBER = "MEMBER"
    LIBRARIAN = "LIBRARIAN"

class User(BaseEntity):
    username: str
    email: EmailStr
    hashed_password: str
    role: UserRole = UserRole.MEMBER
    is_active: bool = True
