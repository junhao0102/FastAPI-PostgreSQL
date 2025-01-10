from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from sqlalchemy.orm import sessionmaker
from .models import Base
from setting import get_settings 

# 從設定檔案中取得應用程式的設定
settings = get_settings()

# 創建一個非同步的資料庫引擎
async_engine = create_async_engine(settings.database_url, echo=True)

#  創建一個非同步的資料庫會話工廠
async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)

""" 為每個請求生成一個資料庫會話 """
async def get_session():
    async with async_session() as session:
        yield session

""" 初始化資料庫函式 """
async def init_db():
    # 使用非同步上下文管理器來管理資料庫連線
    async with async_engine.begin() as conn:
        # 根據模型的定義，在資料庫中創建對應的資料表
        await conn.run_sync(Base.metadata.create_all)



