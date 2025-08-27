"""
Shared utilities and configurations for Vercel API functions
"""
import os
import logging
from datetime import datetime
from openai import OpenAI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure OpenAI
openai_client = None
try:
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        openai_client = OpenAI(api_key=api_key)
except Exception:
    openai_client = None

# Building configuration
BUILDING_CONFIG = {
    'name': os.getenv('BUILDING_NAME', 'Elysia Apartments'),
    'address': os.getenv('BUILDING_ADDRESS', '123 Main Street'),
    'contact': os.getenv('BUILDING_CONTACT', 'manager@elysiaapartments.com'),
    'amenities': [
        'Fitness Center (6 AM - 10 PM)',
        'Rooftop Pool (8 AM - 8 PM)',
        'Business Center (24/7)',
        'Concierge Desk (8 AM - 6 PM)',
        'Package Room (24/7 access)',
        'Parking Garage',
        'Laundry Facilities'
    ],
    'policies': {
        'quiet_hours': '10 PM - 8 AM',
        'guest_policy': 'Guests must be registered at front desk',
        'pet_policy': 'Pets allowed with $200 deposit',
        'maintenance_hours': '9 AM - 5 PM Monday-Friday'
    }
}

# Simple in-memory storage for demo (use database in production)
maintenance_requests = []
events = [
    {
        'id': 1,
        'title': 'Rooftop BBQ',
        'date': '2024-09-01',
        'time': '6:00 PM',
        'location': 'Rooftop Deck',
        'description': 'Monthly community BBQ gathering'
    },
    {
        'id': 2,
        'title': 'Fitness Class',
        'date': '2024-08-30',
        'time': '7:00 AM',
        'location': 'Fitness Center',
        'description': 'Morning yoga session'
    }
]

def get_elysia_response(user_message, context=None):
    """Generate AI response using OpenAI API"""
    try:
        # System prompt that defines Elysia's personality and knowledge
        system_prompt = f"""You are Elysia, an AI concierge for {BUILDING_CONFIG['name']}. 
You are friendly, helpful, and knowledgeable about the building and local area.

Building Information:
- Name: {BUILDING_CONFIG['name']}
- Address: {BUILDING_CONFIG['address']}
- Contact: {BUILDING_CONFIG['contact']}

Amenities:
{chr(10).join(f"- {amenity}" for amenity in BUILDING_CONFIG['amenities'])}

Policies:
- Quiet Hours: {BUILDING_CONFIG['policies']['quiet_hours']}
- Guest Policy: {BUILDING_CONFIG['policies']['guest_policy']}
- Pet Policy: {BUILDING_CONFIG['policies']['pet_policy']}
- Maintenance Hours: {BUILDING_CONFIG['policies']['maintenance_hours']}

You can help with:
- Building information and amenities
- Maintenance requests
- Event information
- Local recommendations
- General assistance

Be conversational, helpful, and personable. If you don't know something specific about the building, offer to connect them with building management."""

        # Check if OpenAI API key is configured
        if not openai_client or not openai_client.api_key:
            return "I'm currently in demo mode. Please configure the OpenAI API key to enable full AI functionality. For now, I can help you with basic building information!"

        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            max_tokens=200,
            temperature=0.7
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        logger.error(f"Error generating AI response: {str(e)}")
        # Fallback responses for common queries
        user_message_lower = user_message.lower()
        
        if "gym" in user_message_lower or "fitness" in user_message_lower:
            return f"Our fitness center is open from 6 AM to 10 PM daily. It's located on the 2nd floor and includes cardio equipment, weights, and exercise machines."
        elif "pool" in user_message_lower:
            return f"The rooftop pool is open from 8 AM to 8 PM. Perfect for a refreshing swim with a great city view!"
        elif "parking" in user_message_lower:
            return f"We have a secure parking garage available for residents. Please contact building management for parking space availability."
        elif "event" in user_message_lower or "activity" in user_message_lower:
            return f"We have several upcoming events! Check out our events section for details. Would you like me to tell you about specific upcoming activities?"
        else:
            return f"I'm here to help! I can assist with building information, amenities, maintenance requests, and more. What would you like to know about {BUILDING_CONFIG['name']}?"

def setup_cors_headers(response):
    """Add CORS headers to response"""
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response