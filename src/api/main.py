from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from datetime import datetime

from src.database.mongo import connect_to_mongo
from src.services.feedbacks import save_feedback
from src.services.incidents import get_incidents
from src.model.predictor import predict_incident
from src.model.retrain_model import retrain
from src.schemas.feedback import FeedbackRequest
from src.schemas.predict import PredictRequest

app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()


@app.get("/health", tags=["Infra"])
async def health_check():
    return {"status": "ok"}


@app.post("/feedback", tags=["Feedback"])
async def submit_feedback(feedback: FeedbackRequest):
    incident = await save_feedback(feedback.incident_id, feedback.correct_category)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return {"message": "✅ Feedback saved successfully"}


@app.post("/predict", tags=["Prediction"])
async def predict(input_data: PredictRequest):
    predicted_category = predict_incident(input_data.description)
    return {
        "description": input_data.description,
        "predicted_category": predicted_category,
        "timestamp": datetime.utcnow()
    }


@app.get("/incidents", tags=["Incidents"])
async def list_incidents(
    category: Optional[str] = None,
    from_date: Optional[datetime] = None,
    to_date: Optional[datetime] = None
):
    results = await get_incidents(category, from_date, to_date)
    return results


@app.post("/retrain", tags=["Model"])
async def retrain_endpoint():
    success = await retrain()
    if success:
        return {"message": "✅ Model retrained and saved"}
    raise HTTPException(status_code=400, detail="⚠️ Retraining failed.")