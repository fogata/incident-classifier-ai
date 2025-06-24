import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os

data = {
    "text": [
        "Cannot login to my account",
        "The printer is not working",
        "Need access to VPN",
        "System crashed after update",
        "Forgot my password"
    ],
    "label": ["login", "hardware", "network", "software", "login"]
}

df = pd.DataFrame(data)

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

pipeline.fit(df["text"], df["label"])

os.makedirs("models", exist_ok=True)
model_path = os.path.join("models", "incident_model.pkl")


joblib.dump(pipeline, model_path)

print(f"Model trained and saved to {model_path}")
