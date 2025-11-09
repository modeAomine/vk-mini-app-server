from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import AppConfig
from database import DatabaseManager
from handlers.user_handler import router as user_router
from handlers.address_handler import router as address_router

class VKApp:
    def __init__(self):
        self.app = FastAPI(
            title=AppConfig.APP_TITLE,
            version=AppConfig.APP_VERSION
        )
        self.db_manager = DatabaseManager()
        self._setup_middleware()
        self._setup_routes()
        self._create_tables()

    def _setup_middleware(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=[
                "https://vk-mini-app-server-3xinm8qg3-modeaomines-projects.vercel.app",  # Замените на ваш домен Vercel
                "http://localhost:3000",
                "http://localhost:5173",  # Vite dev server
                "https://vk.com",
                "https://*.vk.com",
            ],
            allow_credentials=True,
            allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
            allow_headers=["*"],
        )

    def _setup_routes(self):
        self.app.include_router(user_router)
        self.app.include_router(address_router)
        
        @self.app.get("/")
        async def root():
            return {"message": "Hello World"}
            
        @self.app.get("/api/health")
        async def health_check():
            return {"status": "ok", "message": "Server is running"}

    def _create_tables(self):
        self.db_manager.create_tables()

    def get_app(self):
        return self.app

app_instance = VKApp()
app = app_instance.get_app()