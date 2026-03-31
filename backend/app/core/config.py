from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Настройки базы данных
    POSTGRES_DB: str = "cotime"
    POSTGRES_USER: str = "cotime_user"
    POSTGRES_PASSWORD: str = "cotime_password"
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: int = 5432

    # Секретный ключ (потом понадобится для JWT)
    SECRET_KEY: str = "change_me_later"

    @property
    def database_url(self) -> str:
        """
        Собираем строку подключения к базе из частей.
        Типа: postgresql://user:password@host:port/dbname
        """
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        # Говорим: читай значения ещё и из файла .env
        env_file = ".env"


# Один глобальный объект настроек для всего приложения
settings = Settings()
