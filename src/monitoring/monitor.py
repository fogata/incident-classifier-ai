import os
import pandas as pd
import asyncio
from datetime import datetime, timedelta
from motor.motor_asyncio import AsyncIOMotorClient

from evidently import Report
from evidently.presets import DataDriftPreset, DataSummaryPreset  

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017")
DB_NAME = "incident_db"
COLLECTION_NAME = "incidents"
REPORT_OUTPUT = "reports/evidently_report.html"

async def load_data():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    recent_date = datetime.utcnow() - timedelta(days=7)
    cursor = collection.find({"timestamp": {"$gte": recent_date}})
    incidents = await cursor.to_list(length=1000)

    if not incidents:
        print("❌ No data available to generate report.")
        return None

    df = pd.DataFrame(incidents)
    if "_id" in df.columns:
        df.drop(columns=["_id"], inplace=True)
    return df

async def run_monitoring():
    df = await load_data()
    if df is None or df.empty:
        return

    report = Report(metrics=[DataDriftPreset(), DataSummaryPreset()])
    report.run(current_data=df)
    report.save_html(REPORT_OUTPUT)
    print(f"📊 Evidently report saved to: {REPORT_OUTPUT}")

if __name__ == "__main__":
    asyncio.run(run_monitoring())
