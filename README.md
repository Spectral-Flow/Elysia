# Elysia 🏢
**AI-Powered Apartment Concierge System**

Elysia is an intelligent apartment concierge that provides residents with 24/7 assistance for building information, maintenance, events, and smart home control.  
It combines a conversational AI interface with integrations for building management, IoT, and resident services.

---

## 🌟 Features

### Core Functionality
- **🤖 Conversational AI**: Natural language interactions powered by OpenAI GPT-4
- **🏢 Building Information**: Quick access to amenities, policies, and contacts
- **🔧 Maintenance Requests**: Submit, track, and update maintenance tickets
- **📅 Event Management**: Stay informed about upcoming building events
- **📱 Responsive Design**: Works on desktop and mobile

### Smart Capabilities
- **Smart Home Integration**: Control lights, temperature, and IoT devices
- **Personalized Assistance**: Context-aware, resident-specific responses
- **Secure Authentication**: JWT-based user login
- **Voice Interface**: Optional speech-to-text for hands-free interaction
- **Error Handling**: Graceful fallbacks when services are unavailable

---

## 🏗️ Project Structure

```
Elysia/
├── 📁 src/backend/          # Main Flask application
│   └── app.py              # Primary server with all endpoints
├── 📁 ai_core/             # AI chat logic and OpenAI integration
│   ├── __init__.py
│   └── chatbot.py          # ElysiaAI class with conversation handling
├── 📁 templates/           # HTML templates for web interface
│   └── index.html          # Main chat interface page
├── 📁 static/              # Frontend assets
│   ├── css/style.css       # UI styling
│   └── js/app.js          # Chat functionality and interactions
├── 📁 integrations/        # External system integrations
│   ├── __init__.py
│   └── smart_home.py       # Smart home device controls
├── 📁 tests/               # Test suite
│   ├── test_api.py         # API endpoint tests
│   ├── test_app.py         # Application tests
│   └── test_chatbot.py     # AI core tests
├── 📁 docs/                # Documentation
│   ├── architecture.md     # System architecture details
│   └── api.md             # API documentation
├── 📁 backend/             # Alternative backend (legacy)
├── .env.example            # Environment configuration template
├── requirements.txt        # Python dependencies
├── start.sh               # Quick start script
├── Dockerfile             # Container deployment
├── docker-compose.yml     # Multi-service deployment
└── README.md              # This file
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+** 
- **pip** (Python package manager)
- **OpenAI API Key** (optional, for full AI features)

### 1. Clone the Repository

```bash
git clone https://github.com/Spectral-Flow/Elysia.git
cd Elysia
```

### 2. Easy Setup (Recommended)

Use the provided startup script for automatic setup:

```bash
chmod +x start.sh
./start.sh
```

This script will:
- Create a virtual environment
- Install all dependencies
- Copy `.env.example` to `.env`
- Start the application

### 3. Manual Setup

If you prefer manual installation:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Edit .env with your configurations (see Configuration section)
nano .env

# Start the application
python src/backend/app.py
```

### 4. Access the Application

Open your browser and navigate to:
```
http://localhost:5000
```

You should see the Elysia chat interface! 🎉

---

## ⚙️ Configuration

### Environment Variables

Copy `.env.example` to `.env` and configure the following:

```bash
# Flask Configuration
FLASK_APP=src/backend/app.py
FLASK_ENV=development         # Use 'production' for deployment
FLASK_DEBUG=True              # Set to False in production

# OpenAI API (Required for full AI features)
OPENAI_API_KEY=your_openai_api_key_here

# Security (Required for production)
JWT_SECRET_KEY=your_jwt_secret_key_here
SECRET_KEY=your_secret_key_here

# Smart Home Integration (Optional)
SMART_HOME_API_URL=https://api.smarthome.example.com
SMART_HOME_API_KEY=your_smart_home_api_key_here

# Database (Future enhancement)
DATABASE_URL=sqlite:///elysia.db

# Building Configuration
BUILDING_NAME=Elysia Apartments
BUILDING_ADDRESS=123 Main Street, City, State 12345
BUILDING_CONTACT=manager@elysiaapartments.com
```

### Getting an OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key and add it to your `.env` file

**Note:** Elysia works in demo mode without an API key, but AI responses will be limited.

---

## 🎯 Usage Guide

### Chat Interface

1. **Start a Conversation**: Type your question in the chat input
2. **Quick Actions**: Use the sidebar buttons for common requests:
   - 🔧 **Report Maintenance**: Submit maintenance requests
   - 📅 **View Events**: See upcoming building events
   - 🏢 **Building Info**: Access building information
   - 💪 **Gym Hours**: Quick access to amenity hours

### Example Questions

Ask Elysia about:
- "What are the gym hours?"
- "How do I submit a maintenance request?"
- "What events are coming up this month?"
- "What's the guest policy?"
- "Can you help me with my smart home devices?"

### Maintenance Requests

1. Click "🔧 Report Maintenance" or ask in chat
2. Provide details about the issue
3. Specify the location
4. Receive a tracking number for follow-up

---

## 🧪 Testing

Run the test suite to ensure everything is working correctly:

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage report
python -m pytest tests/ --cov=. --cov-report=html

# Run specific test file
python -m pytest tests/test_chatbot.py -v
```

### Test Coverage

The test suite includes:
- **API endpoint testing** (`test_api.py`)
- **Application functionality** (`test_app.py`) 
- **AI chatbot logic** (`test_chatbot.py`)

---

## 🐳 Docker Deployment

### Single Container

```bash
# Build the image
docker build -t elysia .

# Run the container
docker run -p 5000:5000 --env-file .env elysia
```

### Docker Compose (Recommended)

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

---

## ▲ Vercel Deployment

Deploy Elysia to Vercel for scalable, serverless hosting with zero configuration!

### Quick Deploy

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Spectral-Flow/Elysia)

### Manual Deployment

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Deploy to Vercel**:
   ```bash
   vercel
   ```

3. **Set Environment Variables** in Vercel Dashboard:
   - `OPENAI_API_KEY` - Your OpenAI API key
   - `JWT_SECRET_KEY` - Secret for JWT tokens
   - `SECRET_KEY` - Application secret key

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for AI functionality | Yes |
| `JWT_SECRET_KEY` | Secret key for JWT authentication | Yes |
| `SECRET_KEY` | General application secret | Yes |
| `BUILDING_NAME` | Building name (default: "Elysia Apartments") | No |
| `BUILDING_ADDRESS` | Building address | No |
| `BUILDING_CONTACT` | Contact information | No |

### Architecture

- **Frontend**: React app served as static files
- **Backend**: Serverless functions in `/api` directory
- **Database**: In-memory storage (upgrade to Vercel KV for production)

### API Endpoints

After deployment, access your API at:
- `https://your-app.vercel.app/api/chat`
- `https://your-app.vercel.app/api/login`
- `https://your-app.vercel.app/api/maintenance`
- `https://your-app.vercel.app/api/events`
- `https://your-app.vercel.app/api/building-info`

For detailed deployment instructions, see [VERCEL_DEPLOYMENT.md](VERCEL_DEPLOYMENT.md).

---

## 🔧 Development

### Setting Up Development Environment

```bash
# Clone and setup
git clone https://github.com/Spectral-Flow/Elysia.git
cd Elysia

# Create development environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies with development tools
pip install -r requirements.txt

# Set development environment
export FLASK_ENV=development
export FLASK_DEBUG=True

# Run in development mode
python src/backend/app.py
```

### Code Structure

- **Backend**: Flask REST API in `src/backend/app.py`
- **AI Core**: Conversation logic in `ai_core/chatbot.py`
- **Frontend**: HTML/CSS/JS in `templates/` and `static/`
- **Integrations**: External APIs in `integrations/`

### Adding New Features

1. **AI Responses**: Modify `ai_core/chatbot.py`
2. **API Endpoints**: Add routes to `src/backend/app.py`
3. **UI Components**: Edit `templates/index.html` and `static/`
4. **Tests**: Add corresponding test cases

---

## 🌐 API Documentation

### Base URL
```
http://localhost:5000/api
```

### Authentication
Most endpoints require JWT authentication. Include the token in headers:
```
Authorization: <jwt_token>
```

### Endpoints

#### POST `/api/login`
Authenticate user and receive JWT token.

#### POST `/api/chat`
Send message to AI and receive response.

#### POST `/api/maintenance`
Submit maintenance request.

#### GET `/api/events`
Get upcoming building events.

#### GET `/api/building-info`
Get building information and policies.

#### GET `/health`
Health check endpoint for monitoring.

For detailed API documentation, see [`docs/api.md`](docs/api.md).

---

## 🏛️ Architecture

Elysia follows a modular microservices architecture:

- **Frontend**: Responsive web interface
- **Backend API**: Flask REST API with JWT authentication
- **AI Core**: OpenAI GPT-4 integration with conversation management
- **Integrations**: External system connectors (smart home, building management)

For detailed architecture information, see [`docs/architecture.md`](docs/architecture.md).

---

## 🔍 Troubleshooting

### Common Issues

#### "OpenAI API Key not found"
- **Solution**: Add your OpenAI API key to `.env` file
- **Alternative**: Run in demo mode (limited functionality)

#### "Port 5000 already in use"
- **Solution**: Stop other services using port 5000 or change port in configuration

#### "Module not found" errors
- **Solution**: Ensure you're in the virtual environment and dependencies are installed:
  ```bash
  source venv/bin/activate
  pip install -r requirements.txt
  ```

#### Chat not responding
- **Check**: Browser console for JavaScript errors
- **Verify**: Flask server is running and accessible
- **Confirm**: Network connection for API calls

### Health Check

Visit `http://localhost:5000/health` to verify the application is running correctly.

### Logs

Application logs are available in the console output when running in development mode.

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 Python style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting

---

## 📋 Requirements

### System Requirements
- Python 3.10 or higher
- 2GB RAM minimum
- Internet connection (for OpenAI API)

### Python Dependencies
See [`requirements.txt`](requirements.txt) for the complete list.

Key dependencies:
- `flask==2.3.3` - Web framework
- `openai==1.3.5` - AI integration
- `PyJWT==2.8.0` - Authentication
- `pytest==7.4.3` - Testing framework

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/Spectral-Flow/Elysia/issues)
- **Documentation**: [`docs/`](docs/) directory
- **Discussions**: [GitHub Discussions](https://github.com/Spectral-Flow/Elysia/discussions)

---

## 🔮 Roadmap

### Upcoming Features
- [ ] Real-time WebSocket communication
- [ ] Database integration for persistent storage
- [ ] Mobile application
- [ ] Voice interface with speech-to-text
- [ ] Multi-language support
- [ ] Advanced smart home integrations
- [ ] Resident portal with authentication
- [ ] Maintenance request tracking
- [ ] Event RSVP system

---

**Made with ❤️ for modern apartment living**

