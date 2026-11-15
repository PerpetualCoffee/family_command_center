# Loading environment variables (.env) cleanly

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    calendar_url: str
    port: int = 8000

    model_config = SettingsConfigDict(env_file=".env")

    # sanitise icloud calendar link
    @field_validator("calendar_url")
    @classmethod
    def sanitise_webcal(cls, v: str) -> str:
        if v.startswith("webcal://"):
            return v.replace("webcal://", "https://", 1)
        return v

#Instantiate it once right here
settings = Settings()