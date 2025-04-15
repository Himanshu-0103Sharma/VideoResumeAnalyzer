
from pydantic_settings import BaseSettings # Used for defining settings configuration

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    GEMINI_API_KEY: str
    MAX_CONTENT_LENGTH: int = 100 * 1024 * 1024 
    
    class Config:
        env_file = ".env"

settings = Settings()