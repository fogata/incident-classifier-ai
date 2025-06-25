from motor.motor_asyncio import AsyncIOMotorClient
import os

_mongo_client = None

def get_mongo_client():
    if _mongo_client is None:
        raise RuntimeError("Mongo client not initialized. Call connect_to_mongo() first.")
    return _mongo_client

async def connect_to_mongo():
    global _mongo_client
    mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    print(f"🔌 Connecting to MongoDB at: {mongo_url}")
    _mongo_client = AsyncIOMotorClient(mongo_url)
    print("✅ MongoDB connected")

async def close_mongo_connection():
    global _mongo_client
    if _mongo_client:
        _mongo_client.close()
        print("🔌 MongoDB connection closed")
