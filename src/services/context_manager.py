from src.models.context import Context, Message
from src.services.token_counter import count_tokens
from datetime import datetime

class ContextManager:
    def __init__(self, max_tokens: int = 4096):
        self.max_tokens = max_tokens
    
    def trim_context(self, context: Context) -> Context:
        """Trim context to fit within token window."""
        total_tokens = 0
        retained_messages = []
        
        # Start from most recent messages
        for message in reversed(context.messages):
            message_tokens = count_tokens(message.content)
            if total_tokens + message_tokens <= self.max_tokens:
                retained_messages.insert(0, message)
                total_tokens += message_tokens
            else:
                break
                
        context.messages = retained_messages
        context.updated_at = datetime.now()
        
        # Update metadata with token count if MCP metadata exists
        if context.metadata and 'mcp' in context.metadata:
            if 'window' in context.metadata['mcp']:
                context.metadata['mcp']['window']['current_tokens'] = total_tokens
        
        return context
    
    def add_message(self, context: Context, message: Message) -> Context:
        """Add a message to the context and trim if needed."""
        context.messages.append(message)
        context.updated_at = datetime.now()
        return self.trim_context(context)
