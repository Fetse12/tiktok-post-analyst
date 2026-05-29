# Use official lightweight Python image
FROM python:3.10-slim

# Set environment variables to prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8501 (default Streamlit port)
EXPOSE 8501

# Run the Streamlit application
CMD ["streamlit", "run", "tiktok_post_analyst/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
