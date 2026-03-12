# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --default-timeout=1000 -r requirements.txt

COPY . .

# Default command: run tests
CMD ["pytest", "-v"]
