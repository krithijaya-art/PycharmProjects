FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy all projects
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
# Default program to run
RUN chmod +x run_all.sh

CMD ["./run_all.sh"]

