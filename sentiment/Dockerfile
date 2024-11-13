FROM python:3.9-slim

# Set environment variables to avoid interactive prompts
ENV TRANSFORMERS_CACHE=/app/models

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download the model during the build process
RUN python -c "from transformers import pipeline; pipeline('sentiment-analysis')"

# Copy the application code
COPY . .

EXPOSE 8001
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]

