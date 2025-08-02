FROM python:3.11-slim

WORKDIR /app

# Copy only requirements first to leverage Docker layer caching
COPY src/requirements.txt ./requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir --force-reinstall -r requirements.txt

# Then copy the rest of the app
COPY src ./src

# Ensure Python can find all modules in /app/src
ENV PYTHONPATH=/app/src

# Set cache/config dirs to avoid permission errors
ENV HF_HOME=/app/cache
ENV TRANSFORMERS_CACHE=/app/cache/transformers
ENV HF_DATASETS_CACHE=/app/cache/datasets
ENV XDG_CACHE_HOME=/app/cache
ENV XDG_CONFIG_HOME=/app/config
ENV HOME=/app

RUN mkdir -p /app/cache/transformers /app/cache/datasets /app/config

EXPOSE 7860

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "7860"]