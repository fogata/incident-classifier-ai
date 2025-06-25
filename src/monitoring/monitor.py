import os
import pandas as pd
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

async def load_data():
    client = AsyncIOMotorClient(MONGO_URL)
    collection = client["incident_db"]["incidents"]
    cursor = collection.find({}, {
        "description": 1,
        "predicted_category": 1,
        "timestamp": 1,
        "_id": 0
    })
    docs = await cursor.to_list(length=1000)
    client.close()
    return pd.DataFrame(docs)

def run_drift_analysis(df: pd.DataFrame):
    # Dividir base em referência e produção simulada
    if df.empty or len(df) < 10:
        print("⚠️ Not enough data to analyze.")
        return

    # Ordenar por timestamp e dividir
    df_sorted = df.sort_values("timestamp")
    midpoint = len(df_sorted) // 2
    reference = df_sorted.iloc[:midpoint]
    current = df_sorted.iloc[midpoint:]

    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=reference, current_data=current)
    report.save_html("evidently_report.html")
    print("✅ Evidently report saved to evidently_report.html")

if __name__ == "__main__":
    import asyncio
    df = asyncio.run(load_data())
    run_drift_analysis(df)