# Use a base image with Python
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the app code to the container
COPY app.py /app

# Install Flask
RUN pip install flask

# Expose the port your app runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]

