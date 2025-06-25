from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from src.database.mongo import get_mongo_client



async def get_incidents(category: Optional[str], from_date: Optional[datetime], to_date: Optional[datetime]) -> List[dict]:
    db = get_mongo_client()["incident_db"]
    collection = db["incidents"]

    query = {}

    if category:
        query["predicted_category"] = category

    if from_date or to_date:
        time_filter = {}
        if from_date:
            time_filter["$gte"] = from_date
        if to_date:
            time_filter["$lte"] = to_date
        query["timestamp"] = time_filter

    cursor = collection.find(query).sort("timestamp", -1)
    results = await cursor.to_list(length=100)

    # 🔁 Corrigir _id para string
    for doc in results:
        doc["_id"] = str(doc["_id"])

    return results


async def save_incident(description: str, category: str):
    doc = {
        "description": description,
        "predicted_category": category,
        "timestamp": datetime.utcnow()
    }
    db = get_mongo_client()["incident_db"]
    collection = db["incidents"]
    await collection.insert_one(doc)


