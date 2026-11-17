FROM python:3.9-slim
WORKDIR /app
COPY factorial.py .
CMD ["python", "factorial.py"]