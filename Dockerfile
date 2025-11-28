# Stage 1: Builder
FROM python:3.10-slim AS builder
WORKDIR /app
COPY /app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
#COPY /app/app.py .
COPY app/ /app/

EXPOSE 5008
CMD ["python", "/app/app.py"]