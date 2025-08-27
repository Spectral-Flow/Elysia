import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ai_core.chatbot import ElysiaAI

def test_elysia_initialization():
    """Test that ElysiaAI initializes correctly."""
    elysia = ElysiaAI()
    assert elysia.building_info is not None
    assert "amenities" in elysia.building_info
    assert "policies" in elysia.building_info

def test_building_info_structure():
    """Test the structure of building information."""
    elysia = ElysiaAI()
    building_info = elysia.building_info
    
    # Test amenities
    assert "gym" in building_info["amenities"]
    assert "pool" in building_info["amenities"]
    assert "location" in building_info["amenities"]["gym"]
    assert "hours" in building_info["amenities"]["gym"]
    
    # Test policies
    assert "pets" in building_info["policies"]
    assert "guests" in building_info["policies"]

def test_maintenance_request():
    """Test maintenance request functionality."""
    elysia = ElysiaAI()
    result = elysia.handle_maintenance_request("user123", "Leaky faucet", "Kitchen")
    
    assert "request_id" in result
    assert "status" in result
    assert "estimated_response" in result
    assert result["status"] == "submitted"
    assert result["request_id"].startswith("MR")