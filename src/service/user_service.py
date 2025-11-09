from typing import Optional
from sqlalchemy.orm import Session
from models.user import User
from repo.user_repo import UserRepository
from schemas.user_schema import UserCreate, UserUpdate

class UserService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def get_user_by_vk_id(self, vk_id: int) -> Optional[User]:
        return self.user_repo.get_by_vk_id(vk_id)

    def save_user(self, user_data: UserCreate) -> User:
        return self.user_repo.create_or_update_by_vk_id(user_data.dict())

    def update_phone(self, vk_id: int, phone: str) -> Optional[User]:
        user = self.user_repo.get_by_vk_id(vk_id)
        if user:
            return self.user_repo.update(user, {"phone": phone})
        return None