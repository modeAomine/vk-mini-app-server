from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from service.user_service import UserService
from schemas.user_schema import UserCreate, UserResponse

router = APIRouter(prefix="/api/users", tags=["users"])

@router.get("/vk/{vk_id}", response_model=UserResponse)
def get_user_by_vk_id(vk_id: int, db: Session = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.get_user_by_vk_id(vk_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("", response_model=UserResponse)
def create_or_update_user(user_data: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.save_user(user_data)

@router.patch("/{vk_id}/phone", response_model=UserResponse)
def update_user_phone(vk_id: int, phone: str, db: Session = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.update_phone(vk_id, phone)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user