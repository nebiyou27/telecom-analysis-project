# Use an official Python runtime as a base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "src/visualization/dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]