from fastapi import APIRouter, HTTPException
from src.services.incidents import get_incidents
from typing import Optional
from datetime import datetime


router = APIRouter()

@router.get("/incidents", tags=["Incidents"])
async def list_incidents(
    category: Optional[str] = None,
    from_date: Optional[datetime] = None,
    to_date: Optional[datetime] = None
):
    results = await get_incidents(category, from_date, to_date)
    return results