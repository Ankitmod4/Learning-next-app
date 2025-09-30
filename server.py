from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str = None

items_db:List[Item] = []


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the FastAPI server!"
    }

@app.get("/items")
def read_items():
    return items_db

@app.post("/items", response_model=Item)
def create_item(item: Item):
    items_db.append(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db[index] = updated_item
            return updated_item
    return {"error": "Item not found"}



@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[index]
            return {"message": "Item deleted"}
    return {"error": "Item not found"}



