from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    vk_id: int
    first_name: str
    last_name: str
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    phone: Optional[str] = None
    email: Optional[str] = None

class UserResponse(UserBase):
    id: int
    phone: Optional[str] = None
    email: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True