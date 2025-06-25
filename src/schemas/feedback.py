
from pydantic import BaseModel

class FeedbackInput(BaseModel):
    correct_category: str

class FeedbackRequest(BaseModel):
    incident_id: str
    correct_category: str