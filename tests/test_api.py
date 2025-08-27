import pytest
import json
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login_endpoint(client):
    """Test the login endpoint."""
    response = client.post('/api/login', 
                          json={'email': 'test@example.com', 'password': 'testpass'},
                          content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'token' in data

def test_login_missing_credentials(client):
    """Test login with missing credentials."""
    response = client.post('/api/login', 
                          json={'email': 'test@example.com'},
                          content_type='application/json')
    
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['message'] == 'Could not verify'

def test_chat_without_token(client):
    """Test chat endpoint without authentication token."""
    response = client.post('/api/chat', 
                          json={'message': 'Hello'},
                          content_type='application/json')
    
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['message'] == 'Token is missing!'

def test_maintenance_without_token(client):
    """Test maintenance endpoint without authentication token."""
    response = client.post('/api/maintenance', 
                          json={'issue': 'Leak', 'location': 'Kitchen'},
                          content_type='application/json')
    
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['message'] == 'Token is missing!'