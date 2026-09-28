FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

WORKDIR /app

# Install dependencies with timeout resilience and updated pip
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Copy backend application source
COPY backend/app ./app

EXPOSE 8000

# Start Uvicorn bound to 0.0.0.0
CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
