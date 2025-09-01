
from ..db.database import DB
from ..models.user import User
from ..schemas.user import UserCreate
from ..auth.security import get_password_hash
from ..utils.exceptions import UserNotFoundException

class UserService:

    def get_user_by_username(self, username: str) -> User | None:
        for user_data in DB["users"].values():
            if user_data['username'] == username:
                return User(**user_data)
        return None

    def create_user(self, user_create: UserCreate) -> User:
        if self.get_user_by_username(user_create.username):
            raise ValueError("Username already registered")
        
        hashed_password = get_password_hash(user_create.password)
        user = User(
            username=user_create.username,
            email=user_create.email,
            hashed_password=hashed_password,
            role=user_create.role
        )
        DB["users"][user.id] = user.dict()
        return user
