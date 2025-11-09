import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseConfig:
    DATABASE_URL = os.getenv("DATABASE_URL")
    
class SecurityConfig:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 1440))

class AppConfig:
    APP_TITLE = os.getenv("VITE_APP_TITLE", "VK Mini App")
    APP_VERSION = os.getenv("VITE_APP_VERSION", "1.0.0")
    VK_APP_ID = os.getenv("VITE_VK_APP_ID")