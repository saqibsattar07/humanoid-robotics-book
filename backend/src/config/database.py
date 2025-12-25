from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from qdrant_client import QdrantClient
from .settings import settings
import os

# Database setup - SQLite for local development, PostgreSQL for production
if settings.neon_database_url:
    # Use PostgreSQL (production)
    DATABASE_URL = settings.neon_database_url
    engine = create_engine(DATABASE_URL)
else:
    # Use SQLite (local development)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, "..", "..", "data", "app.db")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)  # Create data directory if it doesn't exist
    DATABASE_URL = f"sqlite:///{db_path}"
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # Required for SQLite

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Qdrant setup
qdrant_client = QdrantClient(
    url=settings.qdrant_url,
    api_key=settings.qdrant_api_key,
    prefer_grpc=False
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()