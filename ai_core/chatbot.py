import openai
from typing import Dict, List, Any
import os

class ElysiaAI:
    def __init__(self):
        self.api_key = os.environ.get("OPENAI_API_KEY")
        openai.api_key = self.api_key
        self.conversation_history = []
        self.building_info = self._load_building_info()
        
    def _load_building_info(self) -> Dict[str, Any]:
        """Load information about the apartment complex."""
        # In production, this would load from a database
        return {
            "amenities": {
                "gym": {"location": "2nd floor", "hours": "5:00 AM - 11:00 PM"},
                "pool": {"location": "3rd floor", "hours": "8:00 AM - 10:00 PM"}
            },
            "policies": {
                "pets": "Allowed with $500 deposit",
                "guests": "Visitors must sign in at front desk"
            }
        }
    
    def process_query(self, user_input: str, user_id: str) -> str:
        """Process user query and generate a response."""
        # Add user input to conversation history
        self.conversation_history.append({"role": "user", "content": user_input})
        
        # Create system message with building context
        system_message = {
            "role": "system", 
            "content": f"You are Elysia, an AI concierge for residents. You have access to the following building information: {self.building_info}"
        }
        
        # Generate response using OpenAI's API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[system_message] + self.conversation_history,
            max_tokens=150,
            temperature=0.7
        )
        
        # Extract and store assistant's response
        assistant_response = response.choices[0].message['content']
        self.conversation_history.append({"role": "assistant", "content": assistant_response})
        
        return assistant_response
    
    def handle_maintenance_request(self, user_id: str, issue: str, location: str) -> Dict[str, Any]:
        """Create a maintenance request in the system."""
        # In production, this would interact with a maintenance tracking system
        request_id = "MR" + str(hash(user_id + issue + location) % 10000)
        return {
            "request_id": request_id,
            "status": "submitted",
            "estimated_response": "24 hours"
        }