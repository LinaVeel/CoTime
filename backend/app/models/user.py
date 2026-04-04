from enum import Enum

from sqlalchemy import Boolean, Column, Integer, String, DateTime, func

from app.models import Base


class Gender(str, Enum):
    MALE = "мужчина"
    FEMALE = "женщина"
    UNSPECIFIED = "не указано"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Профиль
    avatar_url = Column(String, nullable=True)  # ссылка на аватар
    gender = Column(
        String,
        nullable=False,
        default=Gender.UNSPECIFIED.value,  # "не указано" по умолчанию
    )
    age = Column(Integer, nullable=True)
    bio = Column(String, nullable=True)
    city = Column(String, nullable=True)
