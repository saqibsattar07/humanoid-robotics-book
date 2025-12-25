from typing import List, Dict, Any
from ..models.citation import Citation
from ..config.database import SessionLocal
from ..models.document_chunk import DocumentChunk
from sqlalchemy.orm import Session
import logging


logger = logging.getLogger(__name__)


class CitationService:
    def __init__(self):
        pass

    def create_citation_from_chunk(self, chunk_data: Dict[str, Any], relevance_score: float = 1.0) -> Citation:
        """Create a citation from chunk data"""
        return Citation(
            chunk_id=chunk_data.get("chunk_id", ""),
            module=chunk_data.get("module", ""),
            chapter=chunk_data.get("chapter", ""),
            section=chunk_data.get("section", ""),
            page_number=chunk_data.get("page_number", 0),
            text_snippet=chunk_data.get("content", "")[:200] + "..." if len(chunk_data.get("content", "")) > 200 else chunk_data.get("content", ""),
            relevance_score=relevance_score
        )

    def create_citations_from_chunks(self, chunk_results: List[Dict[str, Any]]) -> List[Citation]:
        """Create citations from multiple chunk results"""
        citations = []
        for chunk_result in chunk_results:
            citation = self.create_citation_from_chunk(
                chunk_result,
                relevance_score=chunk_result.get("score", 0.0)
            )
            citations.append(citation)
        return citations

    def get_chunk_content_by_id(self, chunk_id: str) -> str:
        """Get the content of a chunk by its ID from the database"""
        db: Session = SessionLocal()
        try:
            chunk = db.query(DocumentChunk).filter(DocumentChunk.id == chunk_id).first()
            return chunk.content if chunk else ""
        except Exception as e:
            logger.error(f"Error retrieving chunk content: {str(e)}")
            return ""
        finally:
            db.close()

    def format_citations_for_response(self, citations: List[Citation]) -> List[Dict[str, Any]]:
        """Format citations for API response"""
        return [
            {
                "chunk_id": citation.chunk_id,
                "module": citation.module,
                "chapter": citation.chapter,
                "section": citation.section,
                "page_number": citation.page_number,
                "text_snippet": citation.text_snippet,
                "relevance_score": citation.relevance_score
            }
            for citation in citations
        ]