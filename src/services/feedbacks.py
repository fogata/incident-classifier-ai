from bson import ObjectId
from src.database.mongo import get_mongo_client


async def _get_collection():
    
    mongo_client = get_mongo_client()
    return mongo_client["incident_db"]["incidents"]


async def save_feedback(incident_id: str, correct_category: str):

    collection = await _get_collection()
    incident = await collection.find_one({"_id": ObjectId(incident_id)})

    if not incident:
        return None

    await collection.update_one(
        {"_id": ObjectId(incident_id)},
        {"$set": {
            "correct_category": correct_category,
            "feedback_received": True
        }}
    )
    return incident


async def update_feedback(incident_id: str, correct_category: str) -> dict:

    collection = await _get_collection()
    result = await collection.find_one({"_id": ObjectId(incident_id)})

    if not result:
        return {"error": "Incident not found."}

    await collection.update_one(
        {"_id": ObjectId(incident_id)},
        {"$set": {
            "correct_category": correct_category,
            "feedback_received": True
        }}
    )
    return {
        "message": "✅ Feedback recorded.",
        "original_category": result["predicted_category"],
        "correct_category": correct_category
    }
