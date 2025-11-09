from sqlalchemy.orm import Session
from typing import List, Optional
from models.address import Address

class AddressRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_user_id(self, user_id: int) -> List[Address]:
        return self.db.query(Address).filter(Address.user_id == user_id).all()

    def get_by_id(self, address_id: int) -> Optional[Address]:
        return self.db.query(Address).filter(Address.id == address_id).first()

    def create(self, address_data: dict) -> Address:
        address = Address(**address_data)
        self.db.add(address)
        self.db.commit()
        self.db.refresh(address)
        return address

    def delete(self, address_id: int) -> bool:
        address = self.get_by_id(address_id)
        if address:
            self.db.delete(address)
            self.db.commit()
            return True
        return False