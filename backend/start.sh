#!/bin/bash
# Startup script for local development

# Check if running in development mode
if [ "$1" = "dev" ]; then
    echo "Starting in development mode with local Qdrant..."
    export QDRANT_URL="http://localhost:6333"
fi

# Start the FastAPI application
uvicorn src.main:app --reload --port 8000