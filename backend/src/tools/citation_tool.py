from typing import List, Dict, Any
from ..services.citation_service import CitationService
import logging


logger = logging.getLogger(__name__)


class CitationTool:
    """
    Tool for the OpenAI Agent to handle citation generation and formatting
    """
    def __init__(self):
        self.citation_service = CitationService()

    def format_citations(self, citations: List[Dict[str, Any]]) -> str:
        """
        Format citations for inclusion in the response
        """
        try:
            formatted_citations = []
            for citation in citations:
                formatted_citation = (
                    f"Module: {citation.get('module', 'N/A')}, "
                    f"Chapter: {citation.get('chapter', 'N/A')}, "
                    f"Section: {citation.get('section', 'N/A')}, "
                    f"Page: {citation.get('page_number', 'N/A')}"
                )
                formatted_citations.append(formatted_citation)

            return "\n".join([f"[{i+1}] {citation}" for i, citation in enumerate(formatted_citations)])

        except Exception as e:
            logger.error(f"Error formatting citations: {str(e)}")
            return ""

    def validate_citations(self, response: str, citations: List[Dict[str, Any]]) -> bool:
        """
        Validate that the response properly references the citations
        This is a simplified validation - in practice, you'd want more sophisticated checks
        """
        try:
            # Check if response contains citation indicators
            has_citations = any(f"[{i+1}]" in response for i in range(len(citations)))
            return has_citations
        except Exception as e:
            logger.error(f"Error validating citations: {str(e)}")
            return False

    def run(self, citations: List[Dict[str, Any]]) -> str:
        """
        Main method to run the citation tool
        """
        return self.format_citations(citations)