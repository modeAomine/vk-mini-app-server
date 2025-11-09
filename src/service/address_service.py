from typing import List
from sqlalchemy.orm import Session
from models.address import Address
from repo.address_repo import AddressRepository
from schemas.address_schema import AddressCreate

class AddressService:
    def __init__(self, db: Session):
        self.address_repo = AddressRepository(db)

    def get_user_addresses(self, user_id: int) -> List[Address]:
        return self.address_repo.get_by_user_id(user_id)

    def add_address(self, address_data: AddressCreate) -> Address:
        return self.address_repo.create(address_data.dict())

    def delete_address(self, address_id: int) -> bool:
        return self.address_repo.delete(address_id)