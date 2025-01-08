from fastapi import APIRouter
from .info import router as info_router
from .item import router as item_router
from .user import router as user_router


# 建立APIRouter
api_router = APIRouter()

# 註冊子路由
api_router.include_router(info_router)
api_router.include_router(item_router)
api_router.include_router(user_router)
