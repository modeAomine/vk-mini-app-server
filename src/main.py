from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "message": "Server is running"}

# Добавляем простые тестовые endpoints
@app.get("/api/users/{vk_id}")
async def get_user(vk_id: int):
    return {"user_id": vk_id, "name": "Test User"}

@app.post("/api/users")
async def create_user():
    return {"message": "User created"}

@app.get("/api/addresses/user/{user_id}")
async def get_addresses(user_id: int):
    return {"addresses": [], "user_id": user_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)