from typing import Dict, Any
from ..services.retrieval_service import RetrievalService
from ..services.citation_service import CitationService
import logging


logger = logging.getLogger(__name__)


class RAGTool:
    """
    Tool for the OpenAI Agent to perform RAG operations
    """
    def __init__(self):
        self.retrieval_service = RetrievalService()
        self.citation_service = CitationService()

    def retrieve_and_format_context(self, query: str, query_type: str = "full_book", selected_text: str = None) -> Dict[str, Any]:
        """
        Retrieve relevant context and format it for the LLM
        """
        try:
            retrieval_result = self.retrieval_service.retrieve_chunks(
                query=query,
                query_type=query_type,
                selected_text=selected_text
            )

            context_chunks = retrieval_result.get("context_chunks", [])
            citations = retrieval_result.get("citations", [])

            # Build context string
            context_string = self.retrieval_service.build_context_string(context_chunks)

            # Format citations
            formatted_citations = self.citation_service.format_citations_for_response(citations)

            return {
                "context": context_string,
                "citations": formatted_citations,
                "retrieval_time": retrieval_result.get("retrieval_time", 0),
                "chunk_count": len(context_chunks)
            }

        except Exception as e:
            logger.error(f"Error in RAG tool: {str(e)}")
            return {
                "context": "",
                "citations": [],
                "retrieval_time": 0,
                "chunk_count": 0,
                "error": str(e)
            }

    def run(self, query: str, query_type: str = "full_book", selected_text: str = None) -> Dict[str, Any]:
        """
        Main method to run the RAG tool
        """
        return self.retrieve_and_format_context(query, query_type, selected_text)