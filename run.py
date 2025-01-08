import argparse
import asyncio
import uvicorn
from dotenv import load_dotenv

# 解析伺服器運行模式的命令行參數
def parse_server_mode():
    # 創建命令行解析器
    parser = argparse.ArgumentParser(description="Run the server in different modes.")
    # 添加選項參數
    parser.add_argument("--prod", action="store_true", help="Run the server in production mode.")
    parser.add_argument("--test", action="store_true", help="Run the server in test mode.")
    parser.add_argument("--dev", action="store_true", help="Run the server in development mode.")
    return parser.parse_args()

# 根據運行模式動態載入 .env 文件
def load_environment(mode_args):
    if mode_args.prod:
        load_dotenv("./environments/.env.prod")
    elif mode_args.test:
        load_dotenv("./environments/.env.test")
    elif mode_args.dev:
        load_dotenv("./environments/.env.dev")
    else:
        raise ValueError("Please specify a mode using --prod, --test, or --dev.")

if __name__ == "__main__":
    # 解析命令行參數，動態載入環境配置
    args = parse_server_mode()
    load_environment(args)
    
    # 獲取設定並初始化資料庫
    from db import init_db
    from setting import get_settings
    settings = get_settings()
    asyncio.run(init_db())
    
    # 啟動伺服器
    print(f"Starting server in {settings.app_mode} mode...")
    uvicorn.run("main:app", host=settings.host, port=settings.port, reload=settings.reload)