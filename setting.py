import os
from functools import lru_cache

""" 用於管理應用程式配置的 class """
class Settings:
    def __init__(self):
        self.app_name = os.getenv("APP_NAME", "FastAPI App")
        self.app_mode = os.getenv("APP_MODE", "dev")
        self.reload = bool(os.getenv("RELOAD"))
        self.host = os.getenv("HOST", "0.0.0.0")
        self.port = int(os.getenv("PORT", 8000))
        self.database_url = os.getenv("DATABASE_URL")
        
""" 緩存並加載應用的環境設定 """
@lru_cache()
def get_settings():
    return Settings()