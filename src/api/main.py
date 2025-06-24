from fastapi import FastAPI
from dotenv import load_dotenv
import os

from src.database.mongo import connect_to_mongo, close_mongo_connection
from src.database.redis import connect_to_redis, close_redis_connection

load_dotenv()

app = FastAPI(title="Incident Classifier AI", version="0.1")

@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()
    await connect_to_redis()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()
    await close_redis_connection()

@app.get("/health", tags=["Health Check"])
async def health_check():
    return {
        "status": "ok",
        "mongo_url": os.getenv("MONGO_URL"),
        "redis_url": os.getenv("REDIS_URL")
    }
