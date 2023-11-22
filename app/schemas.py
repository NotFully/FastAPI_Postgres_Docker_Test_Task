from typing import List
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    price: float
    photo: str

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

class BuyerBase(BaseModel):
    full_name: str
    purchase_date: str

class BuyerCreate(BuyerBase):
    pass

class Buyer(BuyerBase):
    id: int

    class Config:
        orm_mode = True
