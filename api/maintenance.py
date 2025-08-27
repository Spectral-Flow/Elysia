from datetime import datetime
import json
import os
import sys

# Add the current directory to the path so we can import shared
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from shared import maintenance_requests, logger

def handler(request):
    """Handle maintenance requests for Vercel"""
    
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
        
        request_data = {
            'id': len(maintenance_requests) + 1,
            'unit': data.get('unit', ''),
            'issue': data.get('issue', ''),
            'description': data.get('description', ''),
            'priority': data.get('priority', 'medium'),
            'status': 'submitted',
            'timestamp': datetime.now().isoformat()
        }
        
        maintenance_requests.append(request_data)
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'success': True,
                'request_id': request_data['id'],
                'message': 'Maintenance request submitted successfully'
            })
        }
    
    except Exception as e:
        logger.error(f"Error submitting maintenance request: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': 'Failed to submit maintenance request'})
        }