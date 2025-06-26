from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from src.database.mongo import connect_to_mongo
from src.model.retrain_model import retrain
from src.api.routes import monitor,feedback,feedback,predict,incidents


app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()



@app.get("/health", tags=["Infra"])
async def health_check():
    return {"status": "ok"}

# Modular routers
app.include_router(feedback.router)
app.include_router(monitor.router)
app.include_router(predict.router)
app.include_router(incidents.router)



