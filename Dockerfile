# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the application
COPY . .

# # Expose Flask port
# EXPOSE 5000

# Run the Flask app
ENTRYPOINT ["python3"]
CMD ["app.py", "runserver", "--host=0.0.0.0:5000"]
