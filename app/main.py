from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine, Base
from typing import List


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@app.patch("/api/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    return crud.update_item(db=db, item_id=item_id, item=item)


@app.delete("/api/items/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crud.delete_item(db=db, item_id=item_id)


@app.get("/api/buyers/", response_model=List[schemas.Buyer])
def read_buyers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_buyers(db=db, skip=skip, limit=limit)


@app.get("/api/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db=db, skip=skip, limit=limit)


@app.get("/api/items/{item_id}/buyers/", response_model=List[schemas.Buyer])
def read_buyers_for_item(item_id: int, db: Session = Depends(get_db)):
    return crud.get_buyers_for_item(db=db, item_id=item_id)


@app.get("/api/buyers/{buyer_id}/items/", response_model=List[schemas.Item])
def read_items_for_buyer(buyer_id: int, db: Session = Depends(get_db)):
    return crud.get_items_for_buyer(db=db, buyer_id=buyer_id)
