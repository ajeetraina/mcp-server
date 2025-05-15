import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# Mock API key for testing
client.headers.update({"X-API-Key": "your_secret_api_key"})

def test_create_mcp_context():
    response = client.post("/api/v1/mcp/contexts")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "metadata" in data
    assert "mcp" in data["metadata"]
    assert "window" in data["metadata"]["mcp"]
    assert data["metadata"]["mcp"]["window"]["max_tokens"] == 4096

def test_get_capabilities():
    response = client.get("/api/v1/mcp/capabilities")
    assert response.status_code == 200
    data = response.json()
    assert "version" in data
    assert "capabilities" in data
    assert "token_counting" in data["capabilities"]
