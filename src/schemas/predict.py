from pydantic import BaseModel

class IncidentInput(BaseModel):
    description: str

class IncidentOutput(BaseModel):
    category: str

class PredictRequest(BaseModel):
    description: str