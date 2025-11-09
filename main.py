import sys
import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Добавляем src в путь для импортов
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.database import DatabaseManager, get_db
from src.handlers.user_handler import router as user_router
from src.handlers.address_handler import router as address_router

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VKApp:
    def __init__(self):
        logger.info("Initializing VK App...")
        self.app = FastAPI(title="VK Mini App API", version="1.0.0")
        self.db_manager = DatabaseManager()
        self._setup_middleware()
        self._setup_routes()
        self._create_tables()
        logger.info("VK App initialized successfully")

    def _setup_middleware(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def _setup_routes(self):
        # Подключаем routers из handlers
        self.app.include_router(user_router)
        self.app.include_router(address_router)
        
        # Базовые endpoints для проверки
        @self.app.get("/")
        async def root():
            return {"message": "VK Mini App Server"}
            
        @self.app.get("/api/health")
        async def health_check():
            return {"status": "ok", "message": "Server is running"}

    def _create_tables(self):
        try:
            logger.info("Creating database tables...")
            self.db_manager.create_tables()
            logger.info("Database tables created successfully")
        except Exception as e:
            logger.error(f"Error creating tables: {e}")
            # Не падаем, если таблицы уже созданы
            pass

    def get_app(self):
        return self.app

# Создаем экземпляр приложения
app_instance = VKApp()
app = app_instance.get_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")