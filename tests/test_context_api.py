import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# Mock API key for testing
client.headers.update({"X-API-Key": "your_secret_api_key"})

def test_create_context():
    response = client.post("/api/v1/contexts")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "messages" in data
    assert len(data["messages"]) == 0

def test_add_message():
    # Create context
    response = client.post("/api/v1/contexts")
    context_id = response.json()["id"]
    
    # Add message
    message = {"role": "user", "content": "Hello, world!"}
    response = client.post(f"/api/v1/contexts/{context_id}/messages", json=message)
    assert response.status_code == 200
    data = response.json()
    assert len(data["messages"]) == 1
    assert data["messages"][0]["content"] == "Hello, world!"

def test_get_context():
    # Create context
    response = client.post("/api/v1/contexts")
    context_id = response.json()["id"]
    
    # Get context
    response = client.get(f"/api/v1/contexts/{context_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == context_id

def test_delete_context():
    # Create context
    response = client.post("/api/v1/contexts")
    context_id = response.json()["id"]
    
    # Delete context
    response = client.delete(f"/api/v1/contexts/{context_id}")
    assert response.status_code == 200
    assert response.json() == True
    
    # Verify it's gone
    response = client.get(f"/api/v1/contexts/{context_id}")
    assert response.status_code == 404
