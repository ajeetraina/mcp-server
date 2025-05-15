from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException
from src.storage.context_store import ContextStore
from src.models.context import Message
from src.services.context_manager import ContextManager
import json
from datetime import datetime

ws_router = APIRouter()
context_store = ContextStore()
context_manager = ContextManager()

@ws_router.websocket("/ws/{context_id}")
async def websocket_endpoint(websocket: WebSocket, context_id: str):
    await websocket.accept()
    
    try:
        context = context_store.get_context(context_id)
        if not context:
            await websocket.close(code=1008, reason="Context not found")
            return
            
        # Send initial context
        await websocket.send_text(context.json())
        
        # Listen for updates
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            # Validate message format
            if 'role' not in message_data or 'content' not in message_data:
                await websocket.send_text(json.dumps({
                    "error": "Invalid message format",
                    "required": ["role", "content"]
                }))
                continue
            
            # Create message
            message = Message(
                role=message_data['role'],
                content=message_data['content'],
                timestamp=datetime.now(),
                metadata=message_data.get('metadata')
            )
            
            # Update context
            updated_context = context_manager.add_message(context, message)
            context = context_store.update_context(updated_context)
            
            # Send updated context back
            await websocket.send_text(context.json())
            
    except WebSocketDisconnect:
        pass
    except Exception as e:
        await websocket.close(code=1011, reason=str(e))
