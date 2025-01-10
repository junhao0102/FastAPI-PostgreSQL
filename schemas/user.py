from pydantic import BaseModel

# 定義 User 模型
class CreateUser(BaseModel):
    name: str
    email: str
    password: str 

class CreateUserResponse(BaseModel):
    name: str
    email: str 
    
class ReadUser(BaseModel):
    name: str

class ReadUserResponse(BaseModel):
    name: str 
    email: str
    