from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from .services.agent_service import AgentService
from .config.settings import settings


# Pydantic models for request/response
class ChatRequest(BaseModel):
    query_text: str
    query_type: str = "full_book"  # "full_book" or "selected_text"
    selected_text: Optional[str] = None
    session_id: Optional[str] = None


class ChatResponse(BaseModel):
    response_text: str
    citations: List[Dict[str, Any]]
    grounded: bool
    retrieval_time: Optional[float] = None
    generation_time: Optional[float] = None


class ModelConfigRequest(BaseModel):
    model: str


class ModelConfigResponse(BaseModel):
    current_model: str
    available_models: List[str] = []


# Initialize FastAPI app
app = FastAPI(
    title="RAG Chatbot API",
    description="API for RAG-based question answering from Physical AI & Humanoid Robotics book",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
agent_service = AgentService()


@app.get("/")
def read_root():
    return {"message": "RAG Chatbot API is running!"}


@app.get("/health")
def health_check():
    """Health check endpoint"""
    try:
        is_valid = agent_service.validate_agent_config()
        return {
            "status": "healthy" if is_valid else "configuration error",
            "model_access": is_valid
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e)
        }


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    """Main chat endpoint that processes queries using the agent"""
    try:
        # Process the query through the agent
        agent_response = agent_service.process_query(
            query_text=request.query_text,
            query_type=request.query_type,
            selected_text=request.selected_text
        )

        return ChatResponse(
            response_text=agent_response.content,
            citations=agent_response.citations,
            grounded=agent_response.grounded,
            retrieval_time=agent_response.retrieval_time,
            generation_time=agent_response.generation_time
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")


@app.get("/config/model")
def get_model_config():
    """Get current model configuration"""
    return {
        "current_model": settings.openrouter_model,
        "available_models": []  # In a real implementation, you might fetch available models from OpenRouter
    }


@app.post("/config/model")
def update_model_config(request: ModelConfigRequest):
    """Update model configuration (for development purposes)"""
    # In a real implementation, this might update settings dynamically
    # For now, we'll just return the attempted change
    return {
        "message": "Model configuration would be updated in a real implementation",
        "attempted_model": request.model
    }


# Include API routes
@app.on_event("startup")
def startup_event():
    """Actions to perform on application startup"""
    print(f"Starting RAG Chatbot API with model: {settings.openrouter_model}")
    # Validate agent configuration
    is_valid = agent_service.validate_agent_config()
    if not is_valid:
        print("Warning: Agent configuration validation failed")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)