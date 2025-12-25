from openai import OpenAI
from typing import List
import numpy as np
from ..config.settings import settings
import logging


logger = logging.getLogger(__name__)


class EmbeddingService:
    def __init__(self):
        # Initialize OpenAI client for embeddings
        # In a real implementation with OpenRouter, you might need to use a different embedding provider
        # or local embedding models like sentence-transformers
        self.client = OpenAI(api_key=settings.openrouter_api_key)

    def generate_embedding(self, text: str) -> List[float]:
        """
        Generate embedding for the given text using OpenAI embeddings API.
        In a real OpenRouter setup, you might need to use a different approach for embeddings.
        """
        try:
            # Using OpenAI's text-embedding-3-small model
            # For a real OpenRouter implementation, you might use a different embedding service
            response = self.client.embeddings.create(
                input=text,
                model="text-embedding-3-small"
            )
            return response.data[0].embedding
        except Exception as e:
            logger.error(f"Error generating embedding: {str(e)}")
            # Fallback: return a zero vector
            return [0.0] * 1536

    def generate_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a batch of texts
        """
        return [self.generate_embedding(text) for text in texts]