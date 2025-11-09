from .user_handler import router as user_router
from .address_handler import router as address_router
from .cors_handler import router as cors_router

__all__ = ["user_router", "address_router", "cors_router"]