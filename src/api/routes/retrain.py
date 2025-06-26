
from fastapi import APIRouter, Response
from fastapi import HTTPException
from src.model.retrain_model import retrain
import os

router = APIRouter()


@router.post("/retrain", tags=["Model"])
async def retrain_endpoint():
    success = await retrain()
    if success:
        return {"message": "✅ Model retrained and saved"}
    raise HTTPException(status_code=400, detail="⚠️ Retraining failed.")