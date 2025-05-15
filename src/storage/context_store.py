from typing import Dict, Optional
from src.models.context import Context
import uuid

class ContextStore:
    def __init__(self):
        self.contexts: Dict[str, Context] = {}
    
    def create_context(self) -> Context:
        context_id = str(uuid.uuid4())
        context = Context(id=context_id)
        self.contexts[context_id] = context
        return context
    
    def get_context(self, context_id: str) -> Optional[Context]:
        return self.contexts.get(context_id)
    
    def update_context(self, context: Context) -> Context:
        self.contexts[context.id] = context
        return context
    
    def delete_context(self, context_id: str) -> bool:
        if context_id in self.contexts:
            del self.contexts[context_id]
            return True
        return False
