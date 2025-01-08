from fastapi import APIRouter
from schemas import Item, ItemResponse
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from db.session import get_session
from db.fun import add_item ,select_user
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(tags=["item"],prefix="/api")

# 定義 item get 路由
@router.get("/item/{item_id}", deprecated=True)
def read_item(item_id: int, qry: str = None):
    return {"item_id": item_id, "query": qry }

# 定義 item post 路由
@router.post("/item", response_model=ItemResponse, status_code=201, response_description="Create item successful")
async def create_item(item: Item, session: AsyncSession = Depends(get_session)):
    try:
        user = await select_user(item.owner, session)
        if not user:
            raise HTTPException(status_code=400, detail=f"User with name '{item.owner}' does not exist")
        
        new_item = await add_item(item.name, item.price, item.owner, session)
        return new_item
    except HTTPException as e:
        raise e
    except Exception as e:  
        await session.rollback()  
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
