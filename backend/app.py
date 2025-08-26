from flask import Flask, request, jsonify
import jwt
from datetime import datetime, timedelta, timezone
from functools import wraps
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ai_core.chatbot import ElysiaAI

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("JWT_SECRET_KEY", "dev-secret")

# Initialize Elysia AI
elysia = ElysiaAI()

# User database (replace with real database in production)
users_db = {}

# JWT token required decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = users_db.get(data['user_id'])
            if not current_user:
                return jsonify({'message': 'User not found!'}), 401
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/api/login', methods=['POST'])
def login():
    auth = request.json
    if not auth or not auth.get('email') or not auth.get('password'):
        return jsonify({'message': 'Could not verify'}), 401
    
    # In production, verify against database and use proper password hashing
    user_id = hash(auth.get('email')) % 10000
    
    # Generate token
    token = jwt.encode({
        'user_id': user_id,
        'exp': datetime.now(timezone.utc) + timedelta(hours=24)
    }, app.config['SECRET_KEY'])
    
    return jsonify({'token': token})

@app.route('/api/chat', methods=['POST'])
@token_required
def chat(current_user):
    data = request.json
    user_input = data.get('message', '')
    user_id = current_user['id']
    
    response = elysia.process_query(user_input, user_id)
    
    return jsonify({'response': response})

@app.route('/api/maintenance', methods=['POST'])
@token_required
def maintenance_request(current_user):
    data = request.json
    issue = data.get('issue', '')
    location = data.get('location', '')
    user_id = current_user['id']
    
    result = elysia.handle_maintenance_request(user_id, issue, location)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)