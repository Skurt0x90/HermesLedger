# Dockerfile
# Purpose: Simple image to run a PoA node (for demo).
# It copies src/ into the container and exposes a simple entrypoint.
FROM python:3.11-slim
WORKDIR /app
COPY src/ /app/
CMD ["python", "run_demo.py"]
