from datetime import datetime, timedelta
import json
import os
import sys
import jwt

# Add the current directory to the path so we can import shared
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from shared import logger

def handler(request):
    """Handle login requests for Vercel"""
    
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            },
            'body': ''
        }
    
    if request.method != 'POST':
        return {
            'statusCode': 405,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': 'Method not allowed'})
        }
    
    try:
        # Parse request body
        if hasattr(request, 'json') and request.json:
            data = request.json
        else:
            try:
                data = json.loads(request.body or '{}')
            except:
                data = {}
        
        email = data.get('email', '')
        password = data.get('password', '')
        
        # Simple demo authentication (in production, verify against real user database)
        if email and password:
            # For demo purposes, accept any non-empty email/password
            secret_key = os.getenv('JWT_SECRET_KEY', 'demo_secret_key')
            
            # Create JWT token
            payload = {
                'email': email,
                'exp': datetime.utcnow() + timedelta(hours=24)
            }
            
            token = jwt.encode(payload, secret_key, algorithm='HS256')
            
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({
                    'token': token,
                    'message': 'Login successful'
                })
            }
        else:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({'error': 'Email and password required'})
            }
    
    except Exception as e:
        logger.error(f"Error in login endpoint: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': 'Internal server error'})
        }