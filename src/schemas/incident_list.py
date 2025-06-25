from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class IncidentRecord(BaseModel):
    id: Optional[str] = Field(alias="_id")
    description: str
    predicted_category: str
    timestamp: datetime

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }