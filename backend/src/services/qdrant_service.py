from qdrant_client import QdrantClient
from qdrant_client.http import models
from typing import List, Dict, Any, Optional
from uuid import UUID
import logging
from ..config.settings import settings


logger = logging.getLogger(__name__)


class QdrantService:
    def __init__(self):
        self.client = QdrantClient(
            url=settings.qdrant_url,
            api_key=settings.qdrant_api_key,
            prefer_grpc=False
        )
        self.collection_name = "document_chunks"
        self._ensure_collection_exists()

    def _ensure_collection_exists(self):
        """Ensure the document chunks collection exists with proper configuration"""
        try:
            # Check if collection exists
            self.client.get_collection(self.collection_name)
            logger.info(f"Collection {self.collection_name} already exists")
        except:
            # Create collection if it doesn't exist
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
            )
            logger.info(f"Created collection {self.collection_name}")

            # Create payload index for faster filtering
            self.client.create_payload_index(
                collection_name=self.collection_name,
                field_name="book_id",
                field_schema=models.PayloadSchemaType.KEYWORD
            )

    def store_embedding(self, chunk_id: str, embedding: List[float], metadata: Dict[str, Any]):
        """Store a document chunk embedding in Qdrant"""
        try:
            self.client.upsert(
                collection_name=self.collection_name,
                points=[
                    models.PointStruct(
                        id=chunk_id,
                        vector=embedding,
                        payload={
                            "chunk_id": chunk_id,
                            "book_id": metadata.get("book_id", ""),
                            "module": metadata.get("module", ""),
                            "chapter": metadata.get("chapter", ""),
                            "section": metadata.get("section", ""),
                            "page_number": metadata.get("page_number", 0),
                            "token_count": metadata.get("token_count", 0)
                        }
                    )
                ]
            )
            logger.info(f"Stored embedding for chunk {chunk_id}")
        except Exception as e:
            logger.error(f"Error storing embedding: {str(e)}")
            raise

    def search_similar(self, query_embedding: List[float], top_k: int = 5, book_id: str = None) -> List[Dict[str, Any]]:
        """Search for similar document chunks"""
        try:
            # Prepare filters
            filters = []
            if book_id:
                filters.append(models.FieldCondition(
                    key="book_id",
                    match=models.MatchValue(value=book_id)
                ))

            filter_obj = models.Filter(must=filters) if filters else None

            search_results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                query_filter=filter_obj,
                limit=top_k,
                with_payload=True
            )

            results = []
            for result in search_results:
                results.append({
                    "chunk_id": result.payload.get("chunk_id"),
                    "book_id": result.payload.get("book_id"),
                    "module": result.payload.get("module"),
                    "chapter": result.payload.get("chapter"),
                    "section": result.payload.get("section"),
                    "page_number": result.payload.get("page_number"),
                    "token_count": result.payload.get("token_count"),
                    "score": result.score
                })

            return results

        except Exception as e:
            logger.error(f"Error searching similar chunks: {str(e)}")
            return []

    def delete_chunk(self, chunk_id: str):
        """Delete a specific chunk from the collection"""
        try:
            self.client.delete(
                collection_name=self.collection_name,
                points_selector=models.PointIdsList(
                    points=[chunk_id]
                )
            )
            logger.info(f"Deleted chunk {chunk_id}")
        except Exception as e:
            logger.error(f"Error deleting chunk: {str(e)}")

    def get_chunk(self, chunk_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific chunk by ID"""
        try:
            records = self.client.retrieve(
                collection_name=self.collection_name,
                ids=[chunk_id],
                with_payload=True
            )

            if records:
                record = records[0]
                return {
                    "chunk_id": record.payload.get("chunk_id"),
                    "book_id": record.payload.get("book_id"),
                    "module": record.payload.get("module"),
                    "chapter": record.payload.get("chapter"),
                    "section": record.payload.get("section"),
                    "page_number": record.payload.get("page_number"),
                    "token_count": record.payload.get("token_count")
                }
            return None
        except Exception as e:
            logger.error(f"Error retrieving chunk: {str(e)}")
            return None