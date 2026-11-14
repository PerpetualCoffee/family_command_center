# Loading environment variables (.env) cleanly

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    calendar_url: str
    port: int = 8000

    model_config = SettingsConfigDict(env_file=".env")

#Instantiate it once right here
settings = Settings()