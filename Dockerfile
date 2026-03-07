FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Make root project importable
ENV PYTHONPATH=/app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make script executable
RUN chmod +x run_all.sh

# Default command
CMD ["bash", "run_all.sh"]
