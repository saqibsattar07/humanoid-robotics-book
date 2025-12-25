# Quickstart Guide: Integrated RAG Chatbot

**Feature**: Integrated RAG Chatbot
**Date**: 2025-01-15
**Guide**: Claude AI Assistant

## Overview

This guide provides a quick start for implementing the RAG chatbot system for the Physical AI & Robotics book. Follow these steps to set up the development environment and begin implementation.

## Prerequisites

### System Requirements
- Python 3.11+
- Node.js 18+ (for frontend)
- Docker (for local database setup)
- OpenAI API key
- Qdrant Cloud account
- Neon Postgres account

### Environment Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd humanoid-robotics-book
   ```

2. **Create virtual environment for backend**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install backend dependencies**
   ```bash
   pip install fastapi uvicorn openai qdrant-client psycopg2-binary python-dotenv
   pip install pytest pytest-asyncio  # For testing
   ```

4. **Install frontend dependencies**
   ```bash
   cd frontend
   npm install
   ```

## Configuration

### Environment Variables

Create a `.env` file in the backend root:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Qdrant Configuration
QDRANT_URL=your_qdrant_cloud_url
QDRANT_API_KEY=your_qdrant_api_key
QDRANT_COLLECTION_NAME=document_chunks

# Postgres Configuration
DATABASE_URL=postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname

# Application Settings
BOOK_ID=physical_ai_robotics_book
CHUNK_SIZE_MIN=300
CHUNK_SIZE_MAX=500
RETRIEVAL_TOP_K=5
```

## Backend Setup

### 1. Start the API Server

```bash
cd backend
uvicorn src.main:app --reload --port 8000
```

### 2. Run Database Migrations

```bash
# Using your preferred migration tool or directly with psycopg2
python -c "
import psycopg2
from src.config.settings import DATABASE_URL

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# Create tables (example)
cursor.execute('''
CREATE TABLE IF NOT EXISTS chunks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    content TEXT NOT NULL,
    book_id VARCHAR(255) NOT NULL,
    module VARCHAR(100) NOT NULL,
    chapter VARCHAR(100) NOT NULL,
    page_number INTEGER,
    token_count INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
''')

conn.commit()
cursor.close()
conn.close()
"
```

### 3. Initialize Vector Database

```bash
# Create Qdrant collection
python -c "
from qdrant_client import QdrantClient
from qdrant_client.http import models
from src.config.settings import QDRANT_URL, QDRANT_API_KEY, QDRANT_COLLECTION_NAME

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)

# Create collection if it doesn't exist
try:
    client.create_collection(
        collection_name=QDRANT_COLLECTION_NAME,
        vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
    )
    print('Collection created successfully')
except Exception as e:
    print(f'Collection might already exist: {e}')
"
```

## Frontend Setup

### 1. Start the Development Server

```bash
cd frontend
npm run dev
```

### 2. API Integration

The frontend expects the backend API to be available at `http://localhost:8000/api/v1`.

## Key Implementation Areas

### 1. Document Chunking Service (`src/services/chunking_service.py`)

```python
class ChunkingService:
    def chunk_document(self, text: str, min_tokens: int = 300, max_tokens: int = 500) -> List[DocumentChunk]:
        """Split document text into chunks of specified token size."""
        # Implementation for splitting text into 300-500 token chunks
        pass
```

### 2. Embedding Service (`src/services/embedding_service.py`)

```python
class EmbeddingService:
    def generate_embedding(self, text: str) -> List[float]:
        """Generate embedding vector for text using OpenAI."""
        # Implementation for creating embeddings
        pass
```

### 3. Retrieval Service (`src/services/retrieval_service.py`)

```python
class RetrievalService:
    def retrieve_chunks(self, query: str, top_k: int = 5, query_type: str = "full_book", selected_text: Optional[str] = None) -> List[DocumentChunk]:
        """Retrieve relevant chunks based on query and context."""
        # Implementation for retrieving chunks with proper context isolation
        pass
```

### 4. LLM Service (`src/services/llm_service.py`)

```python
class LLMService:
    def generate_response(self, query: str, context_chunks: List[DocumentChunk]) -> QueryResponse:
        """Generate grounded response with citations."""
        # Implementation for generating responses with proper grounding
        pass
```

## Testing

### Backend Tests
```bash
cd backend
pytest tests/unit/ -v
pytest tests/integration/ -v
```

### Frontend Tests
```bash
cd frontend
npm run test
```

## Running the Complete System

### 1. Start Dependencies
```bash
# Terminal 1: Start backend
cd backend
uvicorn src.main:app --reload --port 8000

# Terminal 2: Start frontend
cd frontend
npm run dev
```

### 2. Load Sample Data
```bash
# Run data loading script
cd backend
python scripts/load_sample_data.py
```

## API Endpoints

### Chat Endpoint
- `POST /api/v1/chat` - Submit query and receive response with citations

Request:
```json
{
  "query_text": "What are the key principles of neural networks?",
  "query_type": "full_book",
  "selected_text": null
}
```

Response:
```json
{
  "response_text": "Neural networks are composed of layers of interconnected nodes...",
  "citations": [
    {
      "module": "Module 4",
      "chapter": "Chapter 4.2",
      "section": "Neural Network Fundamentals",
      "page_number": 125,
      "text_snippet": "A neural network consists of input, hidden, and output layers..."
    }
  ],
  "grounded": true
}
```

### Retrieval Endpoint
- `POST /api/v1/retrieve` - Retrieve relevant chunks without generating response

## Development Workflow

1. **Implement core services** - Start with chunking and embedding
2. **Build API endpoints** - Create basic API structure
3. **Add grounding validation** - Ensure responses are properly grounded
4. **Implement citation system** - Add proper citation functionality
5. **Build frontend** - Create user interface
6. **Test integration** - Verify end-to-end functionality

## Common Issues and Solutions

### Qdrant Connection Issues
- Verify API key and URL are correct
- Check network connectivity to Qdrant Cloud

### Embedding Generation Errors
- Ensure OpenAI API key is valid and has sufficient quota
- Check rate limits and implement retry logic

### Retrieval Performance
- Optimize chunk size based on testing results
- Consider pre-filtering strategies for faster retrieval

## Next Steps

1. Implement the chunking service based on the data model
2. Set up the vector database with sample book content
3. Create the core retrieval logic
4. Build the grounding validation mechanism
5. Develop the frontend interface