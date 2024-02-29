# Use the official Python image as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and its dependencies
RUN pip install flask

# Expose port 8080 to allow communication to the Flask app
EXPOSE 8080

# Run the Python application
CMD ["python", "app.py"]
