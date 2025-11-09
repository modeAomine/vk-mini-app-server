from pydantic import BaseModel
from datetime import datetime

class AddressBase(BaseModel):
    title: str
    address_text: str

class AddressCreate(AddressBase):
    user_id: int

class AddressResponse(AddressBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True