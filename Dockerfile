# Use slim Python image (latest stable in your repo — pick 3.10 here)
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for some Python packages like numpy, psycopg2, etc.)
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ai_core/ ./ai_core/
COPY integrations/ ./integrations/
COPY src/ ./src/
COPY templates/ ./templates/
COPY static/ ./static/

# Create logs directory
RUN mkdir -p logs

# Accept build arguments for secrets
ARG OPENAI_API_KEY
ARG JWT_SECRET_KEY
ARG SECRET_KEY
ARG BUILDING_NAME
ARG BUILDING_ADDRESS
ARG BUILDING_CONTACT
ARG SMART_HOME_API_URL
ARG SMART_HOME_API_KEY

# Set environment variables
ENV FLASK_APP=src/backend/app.py
ENV FLASK_ENV=production
ENV PYTHONPATH=/app
ENV OPENAI_API_KEY=$OPENAI_API_KEY
ENV JWT_SECRET_KEY=$JWT_SECRET_KEY
ENV SECRET_KEY=$SECRET_KEY
ENV BUILDING_NAME=$BUILDING_NAME
ENV BUILDING_ADDRESS=$BUILDING_ADDRESS
ENV BUILDING_CONTACT=$BUILDING_CONTACT
ENV SMART_HOME_API_URL=$SMART_HOME_API_URL
ENV SMART_HOME_API_KEY=$SMART_HOME_API_KEY

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Run the application (Gunicorn with workers and timeout)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120", "src.backend.app:app"]
