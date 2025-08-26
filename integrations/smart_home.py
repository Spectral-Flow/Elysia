import requests
from typing import Dict, Any, List
import os

class SmartHomeIntegration:
    def __init__(self):
        self.base_url = os.environ.get("SMART_HOME_API_URL")
        self.api_key = os.environ.get("SMART_HOME_API_KEY")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def get_apartment_status(self, apartment_id: str) -> Dict[str, Any]:
        """Get status of smart devices in an apartment."""
        endpoint = f"{self.base_url}/apartments/{apartment_id}/status"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def adjust_temperature(self, apartment_id: str, temperature: float) -> Dict[str, Any]:
        """Adjust thermostat temperature."""
        endpoint = f"{self.base_url}/apartments/{apartment_id}/thermostat"
        data = {"target_temperature": temperature}
        response = requests.post(endpoint, json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def toggle_lights(self, apartment_id: str, room: str, state: bool) -> Dict[str, Any]:
        """Turn lights on or off in a specific room."""
        endpoint = f"{self.base_url}/apartments/{apartment_id}/lights/{room}"
        data = {"state": state}
        response = requests.post(endpoint, json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def unlock_door(self, apartment_id: str, door_id: str, user_id: str) -> Dict[str, Any]:
        """Unlock a door (with proper authorization checks)."""
        # In a real system, you would have robust authorization checks here
        endpoint = f"{self.base_url}/apartments/{apartment_id}/doors/{door_id}/unlock"
        data = {"user_id": user_id, "timestamp": get_current_timestamp()}
        response = requests.post(endpoint, json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_energy_usage(self, apartment_id: str, days: int = 30) -> Dict[str, Any]:
        """Get energy usage statistics for an apartment."""
        endpoint = f"{self.base_url}/apartments/{apartment_id}/energy"
        params = {"days": days}
        response = requests.get(endpoint, params=params, headers=self.headers)
        response.raise_for_status()
        return response.json()

def get_current_timestamp():
    """Helper function to get current timestamp in ISO format."""
    from datetime import datetime
    return datetime.utcnow().isoformat() + "Z"