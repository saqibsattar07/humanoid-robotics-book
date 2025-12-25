from typing import Optional
from pydantic import BaseModel


class Citation(BaseModel):
    chunk_id: str
    module: str
    chapter: str
    section: str
    page_number: int
    text_snippet: str
    relevance_score: float