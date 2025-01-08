from pydantic import BaseModel

# 定義 User 模型
class User(BaseModel):
    name: str
    email: str
    password: str 

class UserResponse(BaseModel):
    name: str
    email: str 