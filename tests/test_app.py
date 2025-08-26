import pytest
import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src', 'backend'))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert data['service'] == 'Elysia AI Concierge'

def test_home_page(client):
    """Test the main page loads"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Elysia' in response.data

def test_chat_endpoint(client):
    """Test the chat endpoint"""
    response = client.post('/api/chat', 
                          json={'message': 'Hello'},
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'response' in data
    assert 'timestamp' in data

def test_chat_endpoint_empty_message(client):
    """Test chat endpoint with empty message"""
    response = client.post('/api/chat', 
                          json={'message': ''},
                          content_type='application/json')
    assert response.status_code == 400

def test_building_info_endpoint(client):
    """Test the building info endpoint"""
    response = client.get('/api/building-info')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'name' in data
    assert 'amenities' in data
    assert 'policies' in data

def test_events_endpoint(client):
    """Test the events endpoint"""
    response = client.get('/api/events')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'events' in data
    assert isinstance(data['events'], list)

def test_maintenance_request(client):
    """Test maintenance request submission"""
    maintenance_data = {
        'unit': '101',
        'issue': 'plumbing',
        'description': 'Leaky faucet in kitchen',
        'priority': 'medium'
    }
    response = client.post('/api/maintenance',
                          json=maintenance_data,
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert 'request_id' in data

if __name__ == '__main__':
    pytest.main([__file__])