import logging
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import AppConfig
from database import DatabaseManager
from handlers.user_handler import router as user_router
from handlers.address_handler import router as address_router

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger(__name__)

class VKApp:
    def __init__(self):
        logger.info("Initializing VK App...")
        self.app = FastAPI(
            title=AppConfig.APP_TITLE,
            version=AppConfig.APP_VERSION
        )
        self.db_manager = DatabaseManager()
        self._setup_middleware()
        self._setup_routes()
        self._create_tables()
        logger.info("VK App initialized successfully")

    def _setup_middleware(self):
        logger.info("Setting up CORS middleware...")
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def _setup_routes(self):
        logger.info("Setting up routes...")
        self.app.include_router(user_router)
        self.app.include_router(address_router)
        
        @self.app.get("/")
        async def root():
            logger.info("Root endpoint called")
            return {"message": "Hello World"}
            
        @self.app.get("/api/health")
        async def health_check():
            logger.info("Health check called")
            return {"status": "ok", "message": "Server is running"}

    def _create_tables(self):
        try:
            logger.info("Creating database tables...")
            self.db_manager.create_tables()
            logger.info("Database tables created successfully")
        except Exception as e:
            logger.error(f"Error creating tables: {e}")
            raise

    def get_app(self):
        return self.app

try:
    app_instance = VKApp()
    app = app_instance.get_app()
    logger.info("App instance created successfully")
except Exception as e:
    logger.error(f"Failed to create app: {e}")
    raise

if __name__ == "__main__":
    logger.info("Starting server...")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")