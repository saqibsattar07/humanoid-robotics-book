from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # OpenRouter configuration
    openrouter_api_key: str
    openrouter_model: str = "google/gemini-2.0-flash"

    # Qdrant configuration
    qdrant_url: str
    qdrant_api_key: Optional[str] = None

    # Neon Postgres configuration (optional - defaults to SQLite for local development)
    neon_database_url: Optional[str] = None

    # Application settings
    book_id: str = "physical_ai_robotics_book"
    chunk_size_min: int = 300
    chunk_size_max: int = 500
    retrieval_top_k: int = 5

    class Config:
        env_file = ".env"


settings = Settings()