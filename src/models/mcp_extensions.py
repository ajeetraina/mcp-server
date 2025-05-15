from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class MCPContextWindow(BaseModel):
    max_tokens: int = 4096
    current_tokens: int = 0
    
class MCPContext(BaseModel):
    window: MCPContextWindow
    capabilities: List[str] = ["basic", "structured_data"]
    version: str = "1.0"
