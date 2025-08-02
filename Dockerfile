FROM python:3.11-slim

WORKDIR /app

# Copy only requirements first to leverage Docker layer caching
COPY src/requirements.txt ./requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Then copy the rest of the app
COPY src ./src

# Ensure Python can find all modules in /app
ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
