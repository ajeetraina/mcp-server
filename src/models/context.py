from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class Message(BaseModel):
    role: str
    content: str
    timestamp: datetime = datetime.now()
    metadata: Optional[Dict[str, Any]] = None

class Context(BaseModel):
    id: str
    messages: List[Message] = []
    metadata: Optional[Dict[str, Any]] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
