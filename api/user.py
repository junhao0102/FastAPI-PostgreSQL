from fastapi import APIRouter
from schemas import CreateUser, CreateUserResponse, ReadUser, ReadUserResponse
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from db import get_session
from db.fun import add_user, select_user_by_name
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(tags=["user"],prefix="/api")

""" 定義 user get 路由 """
@router.get("/user", response_model=ReadUserResponse, status_code=200, response_description="Get user successful")
async def read_user(read_user:ReadUser, session: AsyncSession = Depends(get_session)):
    user = await select_user_by_name(read_user.name, session)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")
    return {"name": user.name, "email": user.email}

""" 定義 user post 路由 """
@router.post("/user", response_model=CreateUserResponse, status_code=201, response_description="Create user successful")
async def create_user(create_user: CreateUser,  session: AsyncSession = Depends(get_session)):
    try:
        new_user = await add_user(create_user.name, create_user.email, create_user.password, session)
        return new_user
    # 違反唯一約束
    except IntegrityError as e:
        await session.rollback()
        # 獲取原始錯誤消息
        error_message = str(e.orig) 
        if "email" in error_message:
            raise HTTPException(status_code=400, detail="Email already exists")
        elif "name" in error_message:
            raise HTTPException(status_code=400, detail="Name already exists")
        else:
            raise HTTPException(status_code=400, detail="Integrity error occurred")
    except Exception as e:  
        await session.rollback()  
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

