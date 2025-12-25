from typing import List, Dict, Any, Optional
from ..services.embedding_service import EmbeddingService
from ..services.qdrant_service import QdrantService
from ..services.citation_service import CitationService
from ..config.settings import settings
import time
import logging


logger = logging.getLogger(__name__)


class RetrievalService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.qdrant_service = QdrantService()
        self.citation_service = CitationService()

    def retrieve_chunks(self, query: str, query_type: str = "full_book", selected_text: Optional[str] = None) -> Dict[str, Any]:
        """
        Retrieve relevant chunks based on query type:
        - 'full_book': Use vector search against all book content
        - 'selected_text': Use only the provided selected text
        """
        start_time = time.time()

        if query_type == "selected_text" and selected_text:
            # For selected-text queries, return only the selected text as context
            # Create a mock chunk for the selected text
            context_chunks = [{
                "chunk_id": "selected_text",
                "content": selected_text,
                "module": "Selected Text",
                "chapter": "Selected Text",
                "section": "User Selection",
                "page_number": 0,
                "token_count": len(selected_text.split()),
                "score": 1.0
            }]
            citations = self.citation_service.create_citations_from_chunks(context_chunks)
            retrieval_time = time.time() - start_time

            return {
                "context_chunks": context_chunks,
                "citations": citations,
                "retrieval_time": retrieval_time
            }

        elif query_type == "full_book":
            # For full-book queries, use vector search
            try:
                # Generate embedding for the query
                query_embedding = self.embedding_service.generate_embedding(query)

                # Search for similar chunks
                similar_chunks = self.qdrant_service.search_similar(
                    query_embedding=query_embedding,
                    top_k=settings.retrieval_top_k,
                    book_id=settings.book_id
                )

                # Get full content for each chunk
                context_chunks = []
                for chunk in similar_chunks:
                    # For now, we'll use the metadata from Qdrant
                    # In a real implementation, we'd fetch full content from DB
                    context_chunks.append({
                        "chunk_id": chunk["chunk_id"],
                        "content": f"Module: {chunk['module']}, Chapter: {chunk['chapter']}, Section: {chunk['section']}\nContent would be retrieved from DB here...",
                        "module": chunk["module"],
                        "chapter": chunk["chapter"],
                        "section": chunk["section"],
                        "page_number": chunk["page_number"],
                        "token_count": chunk["token_number"],
                        "score": chunk["score"]
                    })

                citations = self.citation_service.create_citations_from_chunks(similar_chunks)
                retrieval_time = time.time() - start_time

                return {
                    "context_chunks": context_chunks,
                    "citations": citations,
                    "retrieval_time": retrieval_time
                }

            except Exception as e:
                logger.error(f"Error in retrieval: {str(e)}")
                retrieval_time = time.time() - start_time

                # Return empty results with error info
                return {
                    "context_chunks": [],
                    "citations": [],
                    "retrieval_time": retrieval_time,
                    "error": str(e)
                }

        else:
            # Invalid query type
            retrieval_time = time.time() - start_time
            return {
                "context_chunks": [],
                "citations": [],
                "retrieval_time": retrieval_time,
                "error": f"Invalid query type: {query_type}"
            }

    def build_context_string(self, chunks: List[Dict[str, Any]]) -> str:
        """Build a context string from retrieved chunks"""
        context_parts = []
        for i, chunk in enumerate(chunks):
            context_parts.append(
                f"Document {i+1} (Module: {chunk.get('module', 'N/A')}, "
                f"Chapter: {chunk.get('chapter', 'N/A')}, "
                f"Section: {chunk.get('section', 'N/A')}):\n"
                f"{chunk.get('content', '')}\n"
            )
        return "\n".join(context_parts)