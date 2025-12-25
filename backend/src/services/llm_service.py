from openai import OpenAI
from typing import List, Dict, Any
from ..config.settings import settings
import time
import logging


logger = logging.getLogger(__name__)


class OpenRouterLLMService:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=settings.openrouter_api_key
        )
        self.model = settings.openrouter_model

    def generate_response(self, context: str, query: str, system_prompt: str = None) -> str:
        """
        Generate response using OpenRouter API with the specified context and query
        """
        start_time = time.time()

        if system_prompt is None:
            system_prompt = "Answer ONLY from provided context. If information is not in the context, respond with 'Not found in the book.'"

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{query}"}
                ],
                temperature=0.1
            )

            generation_time = time.time() - start_time
            logger.info(f"LLM response generated in {generation_time:.2f}s")

            return response.choices[0].message.content

        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return "Not found in the book."

    def validate_model_access(self) -> bool:
        """
        Validate that we can access the configured model
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": "Test"}],
                max_tokens=5
            )
            return True
        except Exception as e:
            logger.error(f"Model access validation failed: {str(e)}")
            return False