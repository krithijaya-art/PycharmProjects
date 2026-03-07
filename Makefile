# Project variables
IMAGE_NAME=python-projects
CONTAINER_NAME=python-projects-container
PYTHON=python3

# Install dependencies
install:
	pip install -r requirements.txt
# Run all python files locally
run:
	@echo "Running all python projects locally"
	./run_all.sh
# Build Docker image
build:
	@echo "Building Docker image..."
	docker build -t $(IMAGE_NAME) .

# Run docker container
docker-run:
	@echo "Running Docker container..."
	docker run --run $(IMAGE_NAME)

PROJECT_DIR=EmployeeDirectoryManagerProject
PYTHON=python3

test:
	@echo "Running Employee Directory Project"
	cd $(PROJECT_DIR) && pytest -v 

employee-test:
	@echo "Running Employee Directory Project"
	cd $(PROJECT_DIR) && $(PYTHON) employee_directory.py < employee_input.dat > employee_output.log
# Remove docker image
docker-clean:
	docker rmi $(IMAGE_NAME)

# Clean python cache files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +

# Full pipeline
all: build docker-run
