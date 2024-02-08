FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8080"]
