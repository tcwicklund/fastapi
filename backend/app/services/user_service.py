from typing import Optional
from pydantic import BaseModel
from uuid import uuid4

# Mock database
users_db = {}


# Pydantic model for User
class User(BaseModel):
    id: str
    name: str
    email: str


class UserService:
    @staticmethod
    def create_user(name: str, email: str) -> User:
        user_id = str(uuid4())
        user = User(id=user_id, name=name, email=email)
        users_db[user_id] = user
        return user

    @staticmethod
    def get_user(user_id: str) -> Optional[User]:
        return users_db.get(user_id)

    @staticmethod
    def update_user(
        user_id: str, name: Optional[str] = None, email: Optional[str] = None
    ) -> Optional[User]:
        user = users_db.get(user_id)
        if not user:
            return None
        if name:
            user.name = name
        if email:
            user.email = email
        users_db[user_id] = user
        return user
