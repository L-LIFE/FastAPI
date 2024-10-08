# 기본적인 터미널 실행문: uvicorn main:app --reload
#http://127.0.0.1:8000/docs

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}

class Item(BaseModel):
    name: str=Field(..., title="Item Name", min_length=2, max_length=50) #최소 2자, 최대 50자를 가져야 하는 필수 필드
    description: str = Field(None, description="The description of the item", max_length=300) #선택 필드이며, 최대 300자까지 가능
    price: float=Field(..., gt=0, description="The price must be greater than zero") #0보다 커야하며, 필수 필드임
    tag: List[str]= Field(default=[], alias="items-tags") #tag 필드는 선택적이며, 기본적으로 빈 리스트를 갖는다, json에서는 'item-tags'로 나타냄

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item.dict()}
