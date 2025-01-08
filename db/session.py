from sqlalchemy.ext.asyncio import AsyncSession
from db import async_session

# 為每個請求生成一個資料庫會話。
async def get_session():
    async with async_session() as session:
        yield session
