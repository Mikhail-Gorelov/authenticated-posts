from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    SECRET_KEY: str
    ALGORITHM: str

    class Config:
        env_file = Path(__file__).parent.parent / ".env"


settings = Settings()
