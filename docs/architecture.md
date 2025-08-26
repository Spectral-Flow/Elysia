# Elysia AI Concierge - Architecture

## System Overview

Elysia is a modular AI concierge system designed for apartment buildings. The architecture follows a microservices approach with clear separation of concerns.

## Components

### 1. AI Core (`ai_core/`)
- **Purpose**: Contains the main AI logic and OpenAI integration
- **Key Files**: 
  - `chatbot.py`: Main ElysiaAI class with conversation handling
- **Responsibilities**:
  - Process natural language queries
  - Maintain conversation history
  - Handle building information queries
  - Generate maintenance requests

### 2. Backend API (`backend/`)
- **Purpose**: RESTful API server using Flask
- **Key Files**:
  - `app.py`: Main Flask application with routes and JWT authentication
- **Responsibilities**:
  - User authentication and authorization
  - API endpoint management
  - Request/response handling
  - Integration with AI core

### 3. Frontend (`frontend/`)
- **Purpose**: React-based web interface
- **Key Files**:
  - `src/App.js`: Main application component
  - `src/components/ChatInterface.jsx`: Chat UI component
- **Responsibilities**:
  - User interface for chat interactions
  - Authentication flow
  - Real-time messaging
  - Voice input (planned)

### 4. Integrations (`integrations/`)
- **Purpose**: External system integrations
- **Key Files**:
  - `smart_home.py`: Smart home system integration
- **Responsibilities**:
  - Smart home device control
  - Building system integration
  - IoT device management

## Data Flow

1. **User Request**: User submits query through frontend
2. **Authentication**: JWT token validation in backend
3. **AI Processing**: Request forwarded to AI core for processing
4. **Response Generation**: AI generates contextual response
5. **Integration Actions**: If needed, smart home actions are triggered
6. **Response Delivery**: Final response sent back to user

## Security

- JWT-based authentication
- Environment variable configuration
- Input validation and sanitization
- Rate limiting (planned)
- HTTPS in production (planned)

## Scalability Considerations

- Stateless API design
- Database integration (planned)
- Microservice architecture
- Container deployment support
- Load balancing ready

## Future Enhancements

- Database integration for persistent storage
- Real-time WebSocket communication
- Advanced AI features (sentiment analysis, multilingual support)
- Mobile application support
- Advanced building system integrations