
from pydantic import BaseModel, EmailStr
from ..models.user import UserRole

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.MEMBER

class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    is_active: bool | None = None

class UserInDB(UserBase):
    id: str
    role: UserRole
    is_active: bool

    class Config:
        orm_mode = True
