from pydantic import BaseModel

# 定義 Item 模型
class CreateItem(BaseModel):
    name: str
    price: float
    owner: str
    
class CreateItemResponse(BaseModel):
    name: str
    price: float
    owner: str
    
class ReadItem(BaseModel):
    user:str
    
class ReadItemResponse(BaseModel):
    user: str
    item: list