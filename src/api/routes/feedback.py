from fastapi import APIRouter, HTTPException
from src.schemas.feedback import FeedbackRequest
from src.services.feedbacks import save_feedback

router = APIRouter()

@router.post("/feedback", tags=["Feedback"])
async def submit_feedback(feedback: FeedbackRequest):
    incident = await save_feedback(feedback.incident_id, feedback.correct_category)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return {"message": "✅ Feedback saved successfully"}
