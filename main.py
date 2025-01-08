from fastapi import FastAPI
from api import api_router

#　建立 FastAPI 應用
app = FastAPI()

# 掛載統一的路由器到應用
app.include_router(api_router)