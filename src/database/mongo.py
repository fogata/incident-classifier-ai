from motor.motor_asyncio import AsyncIOMotorClient
import os

mongo_client = None

async def connect_to_mongo():
    global mongo_client
    mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    mongo_client = AsyncIOMotorClient(mongo_url)

async def close_mongo_connection():
    mongo_client.close()
