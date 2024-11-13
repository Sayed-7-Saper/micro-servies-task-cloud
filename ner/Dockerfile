FROM python:3.9-slim

ENV TRANSFORMERS_CACHE=/app/models

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download the model during the build process
RUN python -c "from transformers import pipeline; pipeline('ner', aggregation_strategy='simple')"

# Copy the application code
COPY . .

EXPOSE 8002
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8002"]

