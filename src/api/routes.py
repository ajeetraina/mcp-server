from fastapi import APIRouter, HTTPException, Depends
from src.models.context import Context, Message
from src.storage.context_store import ContextStore
from src.services.context_manager import ContextManager
from src.api.security import get_api_key
from typing import List, Optional
import uuid
from datetime import datetime

router = APIRouter()
context_store = ContextStore()
context_manager = ContextManager()

@router.post("/contexts", response_model=Context)
async def create_context(api_key: str = Depends(get_api_key)):
    return context_store.create_context()

@router.get("/contexts/{context_id}", response_model=Context)
async def get_context(context_id: str, api_key: str = Depends(get_api_key)):
    context = context_store.get_context(context_id)
    if not context:
        raise HTTPException(status_code=404, detail="Context not found")
    return context

@router.post("/contexts/{context_id}/messages", response_model=Context)
async def add_message(context_id: str, message: Message, api_key: str = Depends(get_api_key)):
    context = context_store.get_context(context_id)
    if not context:
        raise HTTPException(status_code=404, detail="Context not found")
    
    updated_context = context_manager.add_message(context, message)
    return context_store.update_context(updated_context)

@router.delete("/contexts/{context_id}", response_model=bool)
async def delete_context(context_id: str, api_key: str = Depends(get_api_key)):
    result = context_store.delete_context(context_id)
    if not result:
        raise HTTPException(status_code=404, detail="Context not found")
    return True
