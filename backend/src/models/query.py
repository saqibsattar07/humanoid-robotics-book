from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from ..config.database import Base


class StudentQuery(Base):
    __tablename__ = "queries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(String(255))
    query_text = Column(Text, nullable=False)
    query_type = Column(String(20), nullable=False)  # 'full_book' or 'selected_text'
    selected_text = Column(Text)
    context_chunks = Column(String)  # JSON string of chunk IDs
    session_id = Column(String(255), nullable=False)
    timestamp = Column(DateTime, default=func.now())
    source_page = Column(String(255))


class QueryResponse(Base):
    __tablename__ = "responses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    query_id = Column(UUID(as_uuid=True), ForeignKey("queries.id"), nullable=False)
    response_text = Column(Text, nullable=False)
    citations = Column(String)  # JSON string of citations
    context_chunks = Column(String)  # JSON string of chunk IDs used
    confidence_score = Column(Float)
    grounded = Column(Boolean, default=True)
    generated_at = Column(DateTime, default=func.now())
    tokens_used = Column(Integer)
    retrieval_time = Column(Integer)  # in milliseconds
    generation_time = Column(Integer)  # in milliseconds