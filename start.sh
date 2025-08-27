#!/bin/bash

# Elysia AI Concierge Startup Script

echo "🏢 Starting Elysia AI Concierge..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env file with your OpenAI API key and other configurations"
fi

echo "🚀 Starting Elysia..."
export FLASK_APP=src/backend/app.py
export FLASK_ENV=development

# Run the application
python src/backend/app.py