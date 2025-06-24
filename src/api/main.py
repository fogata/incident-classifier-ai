from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env

app = FastAPI(title="Incident Classifier AI", version="0.1")

@app.get("/health", tags=["Health Check"])
async def health_check():
    return {"status": "ok", "mongo_url": os.getenv("MONGO_URL")}
