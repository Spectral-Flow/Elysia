# Elysia 🏢
**AI-Powered Apartment Concierge System**

Elysia is an intelligent apartment building concierge that acts as a companion and partner for residents, providing 24/7 assistance with building information, maintenance requests, events, and personalized recommendations.

## 🌟 Features

### Core Functionality
- **🤖 AI Chat Interface**: Natural language conversations powered by OpenAI GPT
- **🔧 Maintenance Requests**: Easy submission and tracking of maintenance issues
- **📅 Event Management**: View upcoming building events and activities
- **🏢 Building Information**: Instant access to amenities, policies, and contact info
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices

### Smart Capabilities
- **Personalized Assistance**: Context-aware responses tailored to your building
- **Quick Actions**: One-click access to common tasks
- **Real-time Updates**: Live information about building status and events
- **Error Handling**: Graceful fallbacks when services are unavailable

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key (optional for demo mode)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Spectral-Flow/Elysia.git
   cd Elysia
   ```

2. **Run the startup script**:
   ```bash
   ./start.sh
   ```

3. **Configure your environment** (optional):
   - Edit `.env` file with your OpenAI API key
   - Customize building information and settings

4. **Access Elysia**:
   - Open your browser to `http://localhost:5000`
   - Start chatting with your AI concierge!

### Manual Installation

If you prefer manual setup:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Start the application
python src/backend/app.py
```

## 🏗️ Architecture

```
Elysia/
├── src/
│   └── backend/          # Flask application
│       └── app.py        # Main application file
├── templates/            # HTML templates
│   └── index.html        # Main interface
├── static/              # Static assets
│   ├── css/             # Stylesheets
│   └── js/              # JavaScript files
├── tests/               # Test suite
├── config/              # Configuration files
└── docs/                # Documentation
```

### Technology Stack
- **Backend**: Flask (Python)
- **AI**: OpenAI GPT-3.5/GPT-4
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Deployment**: Docker-ready, cloud-scalable

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Building Information
BUILDING_NAME=Your Apartment Complex
BUILDING_ADDRESS=123 Main Street, City, State 12345
BUILDING_CONTACT=manager@yourapartments.com

# Flask Configuration
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
```

### Customization

#### Building Information
Edit the `BUILDING_CONFIG` in `src/backend/app.py` to customize:
- Amenities and hours
- Building policies
- Contact information
- Local recommendations

#### AI Personality
Modify the system prompt in `get_elysia_response()` to adjust:
- Conversation style
- Knowledge base
- Response format
- Specialized features

## 🧪 Testing

Run the test suite:

```bash
# Activate virtual environment
source venv/bin/activate

# Run tests
python -m pytest tests/ -v
```

### Test Coverage
- API endpoints
- Chat functionality
- Error handling
- Form submissions

## 📱 Usage

### Chat Interface
- Ask questions about building amenities
- Request maintenance assistance
- Get event information
- Seek local recommendations

### Quick Actions
- **🔧 Report Maintenance**: Submit repair requests
- **📅 View Events**: See upcoming activities
- **🏢 Building Info**: Access policies and amenities
- **💪 Gym Hours**: Quick access to facility hours

### Maintenance Requests
1. Click "Report Maintenance"
2. Fill out the form with issue details
3. Receive confirmation and tracking ID
4. Get updates from building management

## 🚀 Deployment

### Development
```bash
python src/backend/app.py
```

### Production

#### Using Gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:5000 src.backend.app:app
```

#### Using Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "src.backend.app:app"]
```

### Cloud Deployment
- **AWS**: Deploy using Elastic Beanstalk or ECS
- **Google Cloud**: Use App Engine or Cloud Run
- **Azure**: Deploy with App Service or Container Instances
- **Heroku**: Simple git-based deployment

## 🔮 Future Enhancements

### Planned Features
- **🔐 User Authentication**: Resident login and personalization
- **🏠 IoT Integration**: Smart home device control
- **📊 Analytics Dashboard**: Usage insights for building management
- **🗣️ Voice Interface**: Speech-to-text and text-to-speech
- **📧 Notifications**: Email and SMS alerts
- **🤝 Community Features**: Resident-to-resident communication

### Integration Opportunities
- **Security Systems**: Access control and visitor management
- **Payment Systems**: Rent and fee processing
- **Local Services**: Restaurant and service recommendations
- **Weather Integration**: Weather-based suggestions
- **Calendar Sync**: Personal schedule integration

## 🤝 Contributing

We welcome contributions! Here's how to get involved:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 for Python code
- Write tests for new features
- Update documentation as needed
- Use meaningful commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: Check our [docs](docs/) folder
- **Issues**: Report bugs on [GitHub Issues](https://github.com/Spectral-Flow/Elysia/issues)
- **Discussions**: Join conversations in [GitHub Discussions](https://github.com/Spectral-Flow/Elysia/discussions)

## 🙏 Acknowledgments

- OpenAI for providing the GPT API
- Flask community for the excellent web framework
- All contributors and early adopters

---

**Made with ❤️ for better apartment living**