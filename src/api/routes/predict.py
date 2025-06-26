from fastapi import APIRouter, HTTPException
from datetime import datetime
from src.schemas.predict import PredictRequest
from src.model.predictor import predict_incident


router = APIRouter()

@router.post("/predict", tags=["Prediction"])
async def predict(input_data: PredictRequest):
    predicted_category = predict_incident(input_data.description)
    return {
        "description": input_data.description,
        "predicted_category": predicted_category,
        "timestamp": datetime.utcnow()
    }