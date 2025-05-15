from fastapi import FastAPI
from src.api.routes import router
from src.api.mcp_routes import mcp_router
from src.api.websocket import ws_router
import uvicorn
import os

app = FastAPI(
    title="MCP Server",
    description="Model Context Protocol Server Implementation",
    version="1.0.0"
)

# Include routers
app.include_router(router, prefix="/api/v1")
app.include_router(mcp_router, prefix="/api/v1")
app.include_router(ws_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "name": "MCP Server",
        "description": "Model Context Protocol Server Implementation",
        "version": "1.0.0",
        "docs_url": "/docs"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("src.main:app", host="0.0.0.0", port=port, reload=True)
