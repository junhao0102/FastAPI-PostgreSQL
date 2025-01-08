from db.models import UserModel
from db.models import ItemModel
from sqlalchemy.future import select

# 尋找 User 函式
async def select_user(name,session):
    query = select(UserModel).where(UserModel.name==name)
    result = await session.execute(query)
    return result.scalars().first()
    
# 添加 User 函式
async def add_user(name, email, password,session):
    new_user = UserModel(name=name, email=email, password=password)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

# 添加 Item 函式
async def add_item(name, price, owner,session):
    new_item = ItemModel(name=name, price=price, owner=owner)
    session.add(new_item)
    await session.commit()
    await session.refresh(new_item)
    return new_item
    