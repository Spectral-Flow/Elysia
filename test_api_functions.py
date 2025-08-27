#!/usr/bin/env python3
"""
Simple test script to validate API functions work
"""
import sys
import os
import json
from datetime import datetime

# Add the API directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'api'))

# Mock request object for testing
class MockRequest:
    def __init__(self, method='GET', body=None, headers=None):
        self.method = method
        self.body = body or ''
        self.headers = headers or {}
        if body and isinstance(body, dict):
            self.json = body
        else:
            self.json = None

def test_health_endpoint():
    """Test health endpoint"""
    print("Testing health endpoint...")
    from api.health import handler
    
    request = MockRequest('GET')
    response = handler(request)
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['status'] == 'healthy'
    assert body['service'] == 'Elysia AI Concierge'
    print("✓ Health endpoint test passed")

def test_events_endpoint():
    """Test events endpoint"""
    print("Testing events endpoint...")
    from api.events import handler
    
    request = MockRequest('GET')
    response = handler(request)
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert 'events' in body
    assert len(body['events']) > 0
    print("✓ Events endpoint test passed")

def test_building_info_endpoint():
    """Test building info endpoint"""
    print("Testing building info endpoint...")
    from api.building_info import handler
    
    request = MockRequest('GET')
    response = handler(request)
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert 'name' in body
    assert 'amenities' in body
    print("✓ Building info endpoint test passed")

def test_chat_endpoint():
    """Test chat endpoint"""
    print("Testing chat endpoint...")
    from api.chat import handler
    
    request = MockRequest('POST', body='{"message": "What are the gym hours?"}')
    request.json = {'message': 'What are the gym hours?'}
    response = handler(request)
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert 'response' in body
    assert 'timestamp' in body
    print("✓ Chat endpoint test passed")

def test_login_endpoint():
    """Test login endpoint"""
    print("Testing login endpoint...")
    from api.login import handler
    
    request = MockRequest('POST', body='{"email": "test@example.com", "password": "password"}')
    request.json = {'email': 'test@example.com', 'password': 'password'}
    response = handler(request)
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert 'token' in body
    print("✓ Login endpoint test passed")

def test_maintenance_endpoint():
    """Test maintenance endpoint"""
    print("Testing maintenance endpoint...")
    from api.maintenance import handler
    
    request = MockRequest('POST', body='{"unit": "101", "issue": "plumbing", "description": "Leaky faucet", "priority": "medium"}')
    request.json = {
        'unit': '101',
        'issue': 'plumbing',
        'description': 'Leaky faucet',
        'priority': 'medium'
    }
    response = handler(request)
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['success'] == True
    assert 'request_id' in body
    print("✓ Maintenance endpoint test passed")

def main():
    """Run all tests"""
    print("Running API endpoint tests...\n")
    
    try:
        test_health_endpoint()
        test_events_endpoint()
        test_building_info_endpoint()
        test_chat_endpoint()
        test_login_endpoint()
        test_maintenance_endpoint()
        
        print("\n✅ All API endpoint tests passed!")
        return True
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)