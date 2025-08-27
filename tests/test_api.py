import pytest
import json
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src', 'backend'))

from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_chat_endpoint(client):
    """Test the chat endpoint with a message."""
    response = client.post('/api/chat', 
                          json={'message': 'Hello, what are the gym hours?'},
                          content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'response' in data
    assert len(data['response']) > 0

def test_chat_endpoint_empty_message(client):
    """Test chat endpoint with empty message."""
    response = client.post('/api/chat', 
                          json={'message': ''},
                          content_type='application/json')
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error'] == 'No message provided'

def test_maintenance_endpoint(client):
    """Test maintenance endpoint."""
    response = client.post('/api/maintenance', 
                          json={'issue': 'Leaky faucet', 'location': 'Kitchen', 'unit': '101'},
                          content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert 'request_id' in data
    assert 'message' in data

def test_building_info_endpoint(client):
    """Test building info endpoint."""
    response = client.get('/api/building-info')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'name' in data
    assert 'amenities' in data
    assert 'policies' in data