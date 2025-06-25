# Dockerfile

FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install ./evidently

# Expose API port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
