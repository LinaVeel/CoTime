from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.models import Base  # ← добавили

engine = create_engine(
    settings.database_url,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ВРЕМЕННО: создаём таблицы при старте (для учебного проекта)
def init_db() -> None:
    Base.metadata.create_all(bind=engine)
