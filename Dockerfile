FROM python:3.13.7-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
WORKDIR /app/src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]