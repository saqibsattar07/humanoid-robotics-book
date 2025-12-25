# Data Model: Integrated RAG Chatbot

**Feature**: Integrated RAG Chatbot
**Date**: 2025-01-15
**Modeler**: Claude AI Assistant

## Overview

This document defines the data models for the RAG chatbot system, including document chunks, metadata, queries, and responses. The models support the core functionality of question answering with proper citations while maintaining isolation between full-book and selected-text queries.

## Core Data Models

### 1. DocumentChunk
Represents a segment of the Physical AI & Robotics book content.

```typescript
interface DocumentChunk {
  id: string;                    // Unique identifier for the chunk
  content: string;               // The actual text content (300-500 tokens)
  book_id: string;              // Reference to the book
  module: string;               // Module identifier (e.g., "Module 4")
  chapter: string;              // Chapter identifier (e.g., "Chapter 4.2")
  section: string;              // Section title (e.g., "Neural Networks")
  page_number: number;          // Page number in the original book
  token_count: number;          // Number of tokens in the content
  embedding: number[];          // Vector embedding for similarity search
  created_at: Date;             // Timestamp of creation
  updated_at: Date;             // Timestamp of last update
}
```

### 2. ChunkMetadata
Metadata for efficient retrieval and citation generation.

```typescript
interface ChunkMetadata {
  chunk_id: string;             // Reference to DocumentChunk
  book_id: string;              // Reference to the book
  module: string;               // Module identifier
  chapter: string;              // Chapter identifier
  section: string;              // Section title
  page_number: number;          // Page number in the original book
  word_count: number;           // Word count for the chunk
  topic_tags: string[];         // Topic tags for the content
  difficulty_level: string;     // Difficulty level (e.g., "beginner", "advanced")
  prerequisite_chunks: string[]; // IDs of prerequisite chunks
  created_at: Date;             // Timestamp of creation
}
```

### 3. StudentQuery
Represents a query from a student with context information.

```typescript
interface StudentQuery {
  id: string;                   // Unique identifier for the query
  student_id: string;           // Identifier for the student (optional)
  query_text: string;           // The actual question text
  query_type: "full_book" | "selected_text"; // Type of query
  selected_text?: string;       // Text selected by student (for selected_text queries)
  context_chunks: string[];     // IDs of chunks used as context
  session_id: string;           // Session identifier for conversation context
  timestamp: Date;              // When the query was submitted
  source_page?: string;         // Page where query originated (for UI context)
}
```

### 4. QueryResponse
Represents the system's response to a student query.

```typescript
interface QueryResponse {
  id: string;                   // Unique identifier for the response
  query_id: string;             // Reference to the original query
  response_text: string;        // The generated response text
  citations: Citation[];        // List of citations used in the response
  context_chunks: DocumentChunk[]; // Chunks that were used to generate the response
  confidence_score: number;     // Confidence score for the response (0-1)
  grounded: boolean;            // Whether the response is properly grounded
  generated_at: Date;           // Timestamp of generation
  tokens_used: number;          // Number of tokens in the response
  retrieval_time: number;       // Time taken for retrieval (ms)
  generation_time: number;      // Time taken for generation (ms)
}
```

### 5. Citation
Represents a citation to a specific part of the book.

```typescript
interface Citation {
  chunk_id: string;             // Reference to the chunk used
  module: string;               // Module identifier
  chapter: string;              // Chapter identifier
  section: string;              // Section title
  page_number: number;          // Page number in the original book
  text_snippet: string;         // Snippet of the cited text
  relevance_score: number;      // Relevance score (0-1) for this citation
}
```

## Database Schema (PostgreSQL)

### chunks table
```sql
CREATE TABLE chunks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content TEXT NOT NULL,
  book_id VARCHAR(255) NOT NULL,
  module VARCHAR(100) NOT NULL,
  chapter VARCHAR(100) NOT NULL,
  section VARCHAR(255),
  page_number INTEGER,
  token_count INTEGER,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### chunk_metadata table
```sql
CREATE TABLE chunk_metadata (
  chunk_id UUID PRIMARY KEY REFERENCES chunks(id),
  word_count INTEGER,
  topic_tags TEXT[],
  difficulty_level VARCHAR(50),
  prerequisite_chunks UUID[],
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### queries table
```sql
CREATE TABLE queries (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  student_id VARCHAR(255),
  query_text TEXT NOT NULL,
  query_type VARCHAR(20) NOT NULL CHECK (query_type IN ('full_book', 'selected_text')),
  selected_text TEXT,
  context_chunks UUID[],
  session_id VARCHAR(255) NOT NULL,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  source_page VARCHAR(255)
);
```

### responses table
```sql
CREATE TABLE responses (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  query_id UUID NOT NULL REFERENCES queries(id),
  response_text TEXT NOT NULL,
  citations JSONB, -- Array of citation objects
  context_chunks UUID[],
  confidence_score DECIMAL(3,2),
  grounded BOOLEAN DEFAULT TRUE,
  generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  tokens_used INTEGER,
  retrieval_time INTEGER, -- in milliseconds
  generation_time INTEGER -- in milliseconds
);
```

## Vector Database Schema (Qdrant)

### Collection: document_chunks
```json
{
  "collection_name": "document_chunks",
  "vectors_config": {
    "size": 1536,
    "distance": "Cosine"
  },
  "payload_schema": {
    "chunk_id": {"type": "keyword"},
    "book_id": {"type": "keyword"},
    "module": {"type": "keyword"},
    "chapter": {"type": "keyword"},
    "section": {"type": "text"},
    "page_number": {"type": "integer"},
    "token_count": {"type": "integer"}
  }
}
```

## Relationships

### DocumentChunk ↔ ChunkMetadata
- One-to-one relationship
- ChunkMetadata provides additional metadata for efficient querying

### StudentQuery → QueryResponse
- One-to-one relationship
- Each query generates one response

### QueryResponse → Citation
- One-to-many relationship
- Each response can have multiple citations

### DocumentChunk in Qdrant
- Each DocumentChunk has a corresponding vector in Qdrant
- Used for similarity search during retrieval

## Constraints and Validation

### Data Integrity
- All content chunks must be between 300-500 tokens
- Citations must reference existing DocumentChunks
- Query responses must be grounded in retrieved context
- Selected-text queries must not use global search

### Performance Considerations
- Indexes on frequently queried fields (module, chapter, book_id)
- Vector indexes in Qdrant for fast similarity search
- Efficient serialization of large text fields

## Migration Strategy

### Initial Load
1. Parse Physical AI & Robotics book into chunks
2. Generate embeddings for each chunk
3. Store chunks in both PostgreSQL and Qdrant
4. Create metadata records in PostgreSQL

### Updates
- Incremental updates when book content changes
- Embedding regeneration for modified chunks
- Consistency between PostgreSQL and Qdrant

## Access Patterns

### Query Retrieval
- By book_id and module/chapter for browsing
- By semantic similarity for search
- By student session for conversation history

### Performance Optimization
- Caching frequently accessed chunks
- Pre-computed embeddings for faster retrieval
- Efficient pagination for large result sets