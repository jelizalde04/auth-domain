FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY config/ ./config/
COPY controllers/ ./controllers/
COPY models/ ./models/
COPY swagger ./swagger/
COPY routes/ ./routes/
COPY services/ ./services/
COPY utils/ ./utils/

EXPOSE 1001

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "1001"]

