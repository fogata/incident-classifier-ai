import joblib
import os


model_path = os.path.join("models", "incident_model.pkl")
model = joblib.load(model_path)

def predict_incident(text: str) -> str:
    return model.predict([text])[0]
