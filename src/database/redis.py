import redis.asyncio as redis
import os

redis_client = None

async def connect_to_redis():
    global redis_client
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
    redis_client = redis.Redis.from_url(redis_url)

async def close_redis_connection():
    await redis_client.close()
