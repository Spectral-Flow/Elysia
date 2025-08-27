# API Documentation

## Overview

The Elysia AI Concierge API provides endpoints for user authentication, chat interactions, and maintenance requests.

## Base URL

```
http://localhost:5000/api
```

## Authentication

All protected endpoints require a JWT token in the Authorization header:

```
Authorization: <jwt_token>
```

## Endpoints

### POST /login

Authenticate a user and receive a JWT token.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password"
}
```

**Response:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### POST /chat

Send a message to Elysia AI and receive a response.

**Headers:**
```
Authorization: <jwt_token>
```

**Request Body:**
```json
{
  "message": "What are the gym hours?"
}
```

**Response:**
```json
{
  "response": "The gym is located on the 2nd floor and is open from 5:00 AM - 11:00 PM."
}
```

### POST /maintenance

Submit a maintenance request.

**Headers:**
```
Authorization: <jwt_token>
```

**Request Body:**
```json
{
  "issue": "Leaky faucet in kitchen",
  "location": "Kitchen"
}
```

**Response:**
```json
{
  "request_id": "MR1234",
  "status": "submitted",
  "estimated_response": "24 hours"
}
```

## Error Responses

**401 Unauthorized:**
```json
{
  "message": "Token is missing!"
}
```

**401 Invalid Token:**
```json
{
  "message": "Token is invalid!"
}
```