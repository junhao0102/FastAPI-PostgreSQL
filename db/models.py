from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

# 創建 Base 類，用於所有模型繼承
Base = declarative_base()

""" 定義 User 模型 """
class UserModel(Base):
    __tablename__ = "user" 

    id = Column(Integer, primary_key=True, index=True)  
    name = Column(String, unique=True, nullable=False) 
    email = Column(String, unique=True, index=True, nullable=False) 
    password = Column(String, nullable=False)  
    
    # 定義與 Item 的一對多關係
    items = relationship("ItemModel", back_populates="owner_user")

""" 定義 Item 模型 """
class ItemModel(Base):
    __tablename__ = "item"  

    id = Column(Integer, primary_key=True, index=True)  
    name = Column(String, nullable=False)  
    price = Column(Float, nullable=False)  
    owner_id = Column(Integer, ForeignKey("user.id"), nullable=False) 
    
    # 定義與 User 的反向關係
    owner_user = relationship("UserModel", back_populates="items")
