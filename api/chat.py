from datetime import datetime
import json
import os
import sys

# Add the current directory to the path so we can import shared
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from shared import get_elysia_response, logger

def handler(request):
    """Handle chat requests for Vercel"""
    
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
        
        user_message = data.get('message', '')
        
        if not user_message:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({'error': 'No message provided'})
            }
        
        # Log the conversation
        logger.info(f"User message: {user_message}")
        
        # Get AI response
        ai_response = get_elysia_response(user_message)
        
        logger.info(f"AI response: {ai_response}")
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'response': ai_response,
                'timestamp': datetime.now().isoformat()
            })
        }
    
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': 'Internal server error'})
        }