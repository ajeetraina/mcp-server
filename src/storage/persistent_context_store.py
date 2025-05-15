import json
import os
from typing import Dict, Optional
from src.models.context import Context
from datetime import datetime

class PersistentContextStore:
    def __init__(self, storage_path: str = "data/contexts"):
        self.storage_path = storage_path
        os.makedirs(storage_path, exist_ok=True)
        self.contexts: Dict[str, Context] = self._load_contexts()
    
    def _load_contexts(self) -> Dict[str, Context]:
        contexts = {}
        for filename in os.listdir(self.storage_path):
            if filename.endswith(".json"):
                context_id = filename.replace(".json", "")
                with open(os.path.join(self.storage_path, filename), "r") as f:
                    context_data = json.load(f)
                    # Convert string timestamps to datetime objects
                    if 'created_at' in context_data:
                        context_data['created_at'] = datetime.fromisoformat(context_data['created_at'])
                    if 'updated_at' in context_data:
                        context_data['updated_at'] = datetime.fromisoformat(context_data['updated_at'])
                    
                    # Convert message timestamps
                    if 'messages' in context_data:
                        for msg in context_data['messages']:
                            if 'timestamp' in msg:
                                msg['timestamp'] = datetime.fromisoformat(msg['timestamp'])
                    
                    contexts[context_id] = Context(**context_data)
        return contexts
    
    def _save_context(self, context: Context):
        with open(os.path.join(self.storage_path, f"{context.id}.json"), "w") as f:
            f.write(context.json())
    
    def create_context(self) -> Context:
        context = Context(id=str(uuid.uuid4()))
        self.contexts[context.id] = context
        self._save_context(context)
        return context
    
    def get_context(self, context_id: str) -> Optional[Context]:
        return self.contexts.get(context_id)
    
    def update_context(self, context: Context) -> Context:
        context.updated_at = datetime.now()
        self.contexts[context.id] = context
        self._save_context(context)
        return context
    
    def delete_context(self, context_id: str) -> bool:
        if context_id in self.contexts:
            del self.contexts[context_id]
            os.remove(os.path.join(self.storage_path, f"{context_id}.json"))
            return True
        return False
