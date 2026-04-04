from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3, max_length=20)
    password: str = Field(min_length=6, max_length=20)

    # Дополнительные поля профиля (все необязательные)
    city: Optional[str] = None
    gender: Optional[str] = None       # "мужчина", "женщина", "не указано"
    age: Optional[int] = Field(default=None, ge=0, le=120)
    bio: Optional[str] = Field(default=None, max_length=500)
    avatar_url: Optional[str] = None