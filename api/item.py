from fastapi import APIRouter
from schemas import CreateItem, CreateItemResponse, ReadItem, ReadItemResponse
from fastapi import HTTPException

from db import get_session
from db.fun import add_item, select_user_by_name, select_item_by_id
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(tags=["item"],prefix="/api")

""" 定義 item get 路由 """
@router.get("/item", status_code=200, description="Get item successful")
async def read_item(read_item: ReadItem, session: AsyncSession = Depends(get_session)):
    user = await select_user_by_name(read_item.user, session)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")
    items = await select_item_by_id(user.id, session)
    return items.all()

""" 定義 item post 路由 """
@router.post("/item", response_model=CreateItemResponse, status_code=201, response_description="Create item successful")
async def create_item(create_item: CreateItem, session: AsyncSession = Depends(get_session)):
    try:
        user = await select_user_by_name(create_item.owner, session)
        if not user:
            raise HTTPException(status_code=404, detail=f"User with name '{create_item.owner}' does not exist")
        new_item = await add_item(create_item.name, create_item.price, user.id, session)
        return {
            "name": new_item.name,
            "price": new_item.price,
            "owner": create_item.owner  
        }
    except HTTPException as e:
        raise e
    except Exception as e:  
        await session.rollback()  
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
