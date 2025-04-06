# Use Python 3.13 slim image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and input file
COPY src/ ./src/
COPY input.txt .

# Command to run the application
CMD ["python", "src/text_processor.py"]
