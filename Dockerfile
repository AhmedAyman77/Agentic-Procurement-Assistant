FROM python:3.11-slim

WORKDIR /app

# Copy only requirements first to leverage Docker layer caching
COPY src/requirements.txt ./requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir --force-reinstall -r requirements.txt

# Then copy the rest of the app
COPY src ./src

# Ensure Python can find all modules in /app/src
ENV PYTHONPATH=/app/src

# Set transformers cache to avoid permission errors
ENV HF_HOME=/app/cache
RUN mkdir -p /app/cache

EXPOSE 7860

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "7860"]
