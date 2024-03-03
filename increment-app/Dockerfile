# Use an official, slim Python base image for reduced size
FROM python:3.9-slim

# Environment variables for optimized Python builds/runtime
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create the working directory
WORKDIR /usr/src/app

# Install dependencies efficiently
COPY requirements.txt ./ 
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port for network access
EXPOSE 3000

# Use gunicorn for production-ready web serving
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:3000", "server:app"]
