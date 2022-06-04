from fastapi import Depends, FastAPI
from app.config import get_settings, Settings

# Viene del curso  testdriven.io 


app = FastAPI()

@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping":"pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }

