Desculpe, mas parece haver um erro na sua solicitação. Você mencionou que gostaria de um API em Node.js, mas as especificações do projeto pedem um desenvolvedor Python especializado em FastAPI. Vou assumir que você gostaria de um API em Python usando FastAPI. Se isso estiver correto, aqui está o código:


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float

store_items = []

@app.post("/items/")
async def create_item(item: Item):
    """
    Create a new item
    """
    store_items.append(item.dict())
    return store_items[-1]

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Get an item by ID
    """
    if item_id < 0 or item_id >= len(store_items):
        raise HTTPException(status_code=404, detail="Item not found")
    return store_items[item_id]