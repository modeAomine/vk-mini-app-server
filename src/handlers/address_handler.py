from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from service.address_service import AddressService
from service.user_service import UserService
from schemas.address_schema import AddressCreate, AddressResponse

router = APIRouter(prefix="/api/addresses", tags=["addresses"])

@router.get("/user/{user_id}", response_model=List[AddressResponse])
def get_user_addresses(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(db)
    address_service = AddressService(db)
    
    user = user_service.get_user_by_vk_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    return address_service.get_user_addresses(user.id)

@router.post("", response_model=AddressResponse)
def create_address(address_data: AddressCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    address_service = AddressService(db)
    
    user = user_service.get_user_by_vk_id(address_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    return address_service.add_address(address_data)

@router.delete("/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    address_service = AddressService(db)
    success = address_service.delete_address(address_id)
    if not success:
        raise HTTPException(status_code=404, detail="Address not found")
    return {"message": "Address deleted successfully"}