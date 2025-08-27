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
# (merge both styles — either repo has /backend or /src/backend)
COPY backend/ ./backend/
COPY ai-core/ ./ai-core/
COPY integrations/ ./integrations/
COPY src/ ./src/

# Create logs directory
RUN mkdir -p logs

# Set environment variables
ENV FLASK_APP=src/backend/app.py
ENV FLASK_ENV=production
ENV PYTHONPATH=/app

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Run the application (Gunicorn with workers and timeout)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120", "src.backend.app:app"]
