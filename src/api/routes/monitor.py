from fastapi import APIRouter, Response
import os

router = APIRouter()

@router.get("/monitor/report", response_class=Response)
async def get_monitor_report():
    report_path = "src/monitoring/reports/evidently_report.html"
    if not os.path.exists(report_path):
        return Response(content="Report not found", status_code=404)
    
    with open(report_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    return Response(content=html_content, media_type="text/html")
