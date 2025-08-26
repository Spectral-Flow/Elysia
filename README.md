# Elysia AI Concierge

Elysia is an AI-powered concierge system for apartment buildings that provides residents with intelligent assistance for common tasks, building information, and smart home controls.

## Features

- **Conversational AI Interface**: Natural language processing powered by OpenAI GPT-4
- **Building Information System**: Access to amenities, policies, and building services
- **Maintenance Requests**: Submit and track maintenance requests
- **Smart Home Integration**: Control lights, temperature, and other connected devices
- **Voice Interface**: Speech-to-text capabilities for hands-free interaction
- **Secure Authentication**: JWT-based user authentication system

## Project Structure

```
elysia-ai/
├── backend/                # Flask API backend
├── frontend/               # React frontend application
├── ai-core/                # AI model and NLP components
├── integrations/           # Building systems integration
├── docs/                   # Documentation
├── tests/                  # Test suite
└── infrastructure/         # Deployment configurations
```

## Quick Start

### Prerequisites

- Python 3.10+
- Node.js 16+
- OpenAI API key

### Backend Setup

1. Clone the repository:
```bash
git clone https://github.com/Spectral-Flow/Elysia.git
cd Elysia
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your OpenAI API key and other configuration
```

5. Run the backend server:
```bash
cd backend
python app.py
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install Node.js dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

### Running Tests

```bash
# Python tests
pytest

# Frontend tests
cd frontend
npm test
```

## API Endpoints

### Authentication
- `POST /api/login` - User login and JWT token generation

### Chat Interface
- `POST /api/chat` - Send message to Elysia AI (requires authentication)

### Maintenance
- `POST /api/maintenance` - Submit maintenance request (requires authentication)

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key
- `JWT_SECRET_KEY`: Secret key for JWT token signing
- `SMART_HOME_API_URL`: URL for smart home system integration
- `SMART_HOME_API_KEY`: API key for smart home system

## Docker Deployment

Build and run with Docker:

```bash
docker build -t elysia-ai .
docker run -p 5000:5000 --env-file .env elysia-ai
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please open an issue on GitHub or contact the development team. 
