from db.models import UserModel
from db.models import ItemModel
from sqlalchemy.future import select

""" 利用 name 搜尋 User """
async def select_user_by_name(name,session):
    query = select(UserModel).where(UserModel.name==name)
    result = await session.execute(query)
    return result.scalars().first()

""" 利用 owner_id 搜尋 Item """
async def select_item_by_id(owner_id,session):
    query = select(ItemModel).where(ItemModel.owner_id==owner_id)
    result = await session.execute(query)
    return result.scalars()

""" 添加 User """
async def add_user(name, email, password,session):
    new_user = UserModel(name=name, email=email, password=password)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

""" 添加 Item """
async def add_item(name, price, owner_id,session):
    new_item = ItemModel(name=name, price=price,owner_id=owner_id)
    session.add(new_item)
    await session.commit()
    await session.refresh(new_item)
    return new_item

