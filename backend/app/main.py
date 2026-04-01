from fastapi import FastAPI

from app.core.config import settings
from app.db import init_db  # ← новый импорт

app = FastAPI(title="CoTime API")


@app.on_event("startup")
def on_startup() -> None:
    """
    Эта функция запустится один раз при старте приложения.
    Здесь мы создаём таблицы в базе.
    """
    init_db()


@app.get("/")
def root():
    return {
        "message": "CoTime backend is running",
        "database_url_example": settings.database_url,
    }
