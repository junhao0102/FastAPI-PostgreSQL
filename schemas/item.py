from pydantic import BaseModel

# 定義 Item 模型
class Item(BaseModel):
    name: str
    price: float
    owner: str
    
class ItemResponse(BaseModel):
    name: str
    price: float
    owner: str