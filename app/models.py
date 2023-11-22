from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    photo = Column(String)

    # Отношение с PurchasedItem
    purchases = relationship("PurchasedItem", back_populates="item")


class Buyer(Base):
    __tablename__ = "buyers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    purchase_date = Column(DateTime)

    # Отношение с PurchasedItem
    items = relationship("PurchasedItem", back_populates="buyer")


class PurchasedItem(Base):
    __tablename__ = "purchased_items"

    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey("buyers.id"))
    item_id = Column(Integer, ForeignKey("items.id"))

    # Отношения с Buyer и Item
    buyer = relationship("Buyer", back_populates="items")
    item = relationship("Item", back_populates="purchases")
