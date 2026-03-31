from fastapi import FastAPI

from app.core.config import settings  # импортируем наши настройки


app = FastAPI(title="CoTime API")


@app.get("/")
def root():
    return {
        "message": "CoTime backend is running",
        "database_url_example": settings.database_url,
    }