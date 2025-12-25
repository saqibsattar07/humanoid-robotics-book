@echo off
REM Startup script for local development

REM Check if running in development mode
if "%1"=="dev" (
    echo Starting in development mode with local Qdrant...
    set QDRANT_URL=http://localhost:6333
)

REM Start the FastAPI application
python -m uvicorn src.main:app --reload --port 8000