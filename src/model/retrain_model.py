import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import os
import mlflow
import mlflow.sklearn

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000")

async def get_feedback_data():
    client = AsyncIOMotorClient(MONGO_URL)
    collection = client["incident_db"]["incidents"]
    cursor = collection.find({"feedback_received": True})
    results = await cursor.to_list(length=1000)
    client.close()
    return pd.DataFrame([{
        "text": doc["description"],
        "label": doc["correct_category"]
    } for doc in results if "correct_category" in doc])

async def retrain():
    df = await get_feedback_data()

    if df.empty:
        print("⚠️ No feedback data available.")
        return

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression())
    ])

    pipeline.fit(df["text"], df["label"])

    os.makedirs("models", exist_ok=True)
    model_path = os.path.join("models", "incident_model.pkl")
    joblib.dump(pipeline, model_path)
    print(f"✅ Model retrained and saved to: {model_path}")

    # Log with MLflow
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.set_experiment("incident_classifier")

    with mlflow.start_run(run_name="retrain_via_feedback"):
        mlflow.log_param("model_type", "LogisticRegression")
        mlflow.log_param("feedback_count", len(df))
        accuracy = pipeline.score(df["text"], df["label"])
        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(pipeline, "model")
        mlflow.log_artifact(model_path)
        print("📦 Model and metrics logged to MLflow.")

if __name__ == "__main__":
    asyncio.run(retrain())