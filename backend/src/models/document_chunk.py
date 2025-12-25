from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from ..config.database import Base


class DocumentChunk(Base):
    __tablename__ = "chunks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = Column(Text, nullable=False)
    book_id = Column(String(255), nullable=False)
    module = Column(String(100), nullable=False)
    chapter = Column(String(100), nullable=False)
    section = Column(String(255))
    page_number = Column(Integer)
    token_count = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())