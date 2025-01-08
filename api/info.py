from fastapi import APIRouter
from setting import get_settings

router = APIRouter(tags=["info"],prefix="/api")

# 定義 info get 路由
@router.get("/info")
def read_info():
    settings = get_settings()
    return {
        "app_name": settings.app_name,
        "app_mode": settings.app_mode,
        "reload": settings.reload,
        "host": settings.host,
        "port": settings.port
    }