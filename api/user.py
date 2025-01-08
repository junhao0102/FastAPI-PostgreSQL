from fastapi import APIRouter
from schemas import User, UserResponse
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from db.session import get_session
from db.fun import add_user
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(tags=["user"],prefix="/api")

# 定義 user get 路由
@router.get("/users/{user_id}")
async def read_user(user_id: int, qry: str = None):
    return {"user_id": user_id, "query": qry }

# 定義 user post 路由
@router.post("/user", response_model=UserResponse, status_code=201, response_description="Create user successful")
async def create_user(user: User,  session: AsyncSession = Depends(get_session)):
    try:
        new_user = await add_user(user.name, user.email, user.password, session)
        return new_user
    except IntegrityError:
        await session.rollback()  
        raise HTTPException(status_code=400, detail="Email already exists")
    except Exception as e:  
        await session.rollback()  
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

