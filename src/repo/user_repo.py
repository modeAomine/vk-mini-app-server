from sqlalchemy.orm import Session
from typing import Optional
from models.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_vk_id(self, vk_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.vk_id == vk_id).first()

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()

    def create(self, user_data: dict) -> User:
        user = User(**user_data)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update(self, user: User, update_data: dict) -> User:
        for key, value in update_data.items():
            setattr(user, key, value)
        self.db.commit()
        self.db.refresh(user)
        return user

    def create_or_update_by_vk_id(self, user_data: dict) -> User:
        existing_user = self.get_by_vk_id(user_data['vk_id'])
        if existing_user:
            return self.update(existing_user, user_data)
        return self.create(user_data)