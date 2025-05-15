from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from typing import Optional
import os

API_KEY_NAME = "X-API-Key"
# In production, use environment variables
API_KEY = os.environ.get("API_KEY", "your_secret_api_key")

api_key_header = APIKeyHeader(name=API_KEY_NAME)

async def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    return api_key
