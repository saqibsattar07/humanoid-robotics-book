from openai import OpenAI
from typing import List, Dict, Any
from ..config.settings import settings
from ..services.llm_service import OpenRouterLLMService
from ..services.retrieval_service import RetrievalService
from ..services.citation_service import CitationService
from ..models.agent import AgentConfig, AgentResponse
import time
import logging


logger = logging.getLogger(__name__)


class AgentService:
    def __init__(self):
        self.llm_service = OpenRouterLLMService()
        self.retrieval_service = RetrievalService()
        self.citation_service = CitationService()

    def process_query(self, query_text: str, query_type: str = "full_book", selected_text: str = None) -> AgentResponse:
        """
        Process a query using the agent with proper context retrieval and citation generation
        """
        start_time = time.time()

        # Retrieve relevant context based on query type
        retrieval_result = self.retrieval_service.retrieve_chunks(
            query=query_text,
            query_type=query_type,
            selected_text=selected_text
        )

        retrieval_time = retrieval_result.get("retrieval_time", 0)

        if retrieval_result.get("error"):
            logger.error(f"Retrieval error: {retrieval_result['error']}")
            return AgentResponse(
                content="Not found in the book.",
                citations=[],
                grounded=False,
                retrieval_time=retrieval_time,
                generation_time=0
            )

        # Build context string from retrieved chunks
        context_chunks = retrieval_result["context_chunks"]
        context_string = self.retrieval_service.build_context_string(context_chunks)

        # Generate response using LLM
        generation_start = time.time()
        response_text = self.llm_service.generate_response(
            context=context_string,
            query=query_text
        )
        generation_time = time.time() - generation_start

        # Format citations for response
        citations = self.citation_service.format_citations_for_response(
            retrieval_result["citations"]
        )

        # Check if response indicates no found content
        grounded = "not found in the book" not in response_text.lower()

        total_time = time.time() - start_time

        return AgentResponse(
            content=response_text,
            citations=citations,
            grounded=grounded,
            retrieval_time=retrieval_time,
            generation_time=generation_time
        )

    def validate_agent_config(self) -> bool:
        """
        Validate that the agent can access the configured model
        """
        return self.llm_service.validate_model_access()