from fastapi import APIRouter, HTTPException, Depends
from src.models.context import Context
from src.models.mcp_extensions import MCPContext, MCPContextWindow
from src.storage.context_store import ContextStore
from src.services.context_manager import ContextManager
from src.api.security import get_api_key

mcp_router = APIRouter()
context_store = ContextStore()
context_manager = ContextManager()

@mcp_router.post("/mcp/contexts", response_model=Context)
async def create_mcp_context(api_key: str = Depends(get_api_key)):
    context = context_store.create_context()
    # Add MCP-specific metadata
    context.metadata = {
        "mcp": MCPContext(
            window=MCPContextWindow(
                max_tokens=4096,
                current_tokens=0
            )
        ).dict()
    }
    return context_store.update_context(context)

@mcp_router.get("/mcp/contexts/{context_id}", response_model=Context)
async def get_mcp_context(context_id: str, api_key: str = Depends(get_api_key)):
    context = context_store.get_context(context_id)
    if not context:
        raise HTTPException(status_code=404, detail="Context not found")
    return context

@mcp_router.get("/mcp/capabilities", response_model=dict)
async def get_capabilities(api_key: str = Depends(get_api_key)):
    return {
        "version": "1.0",
        "capabilities": [
            "basic",
            "structured_data",
            "token_counting",
            "context_window_management"
        ]
    }
