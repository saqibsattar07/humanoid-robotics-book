from typing import List, Optional
from pydantic import BaseModel


class AgentConfig(BaseModel):
    model: str
    temperature: float = 0.1
    max_tokens: int = 1000
    tools: List[str] = []
    system_prompt: str = "You are an AI assistant that answers questions based only on the provided context from the Physical AI & Humanoid Robotics book. Only use information from the context provided. If the answer is not in the context, respond with 'Not found in the book.'"


class AgentResponse(BaseModel):
    content: str
    citations: List[dict]
    grounded: bool = True
    retrieval_time: Optional[float] = None
    generation_time: Optional[float] = None