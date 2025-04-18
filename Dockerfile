# Dockerfile

# 1. Base Image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy all files into container
COPY . /app

# 4. Install system dependencies
RUN apt-get update && \
    apt-get install -y build-essential libgl1-mesa-glx && \
    apt-get clean

# 5. Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 6. Expose necessary port
EXPOSE 5001

# 7. Run both Flask + Streamlit servers (simple dev mode with bash)
CMD ["bash", "-c", "python agentic_ts_forecasting_system.py & streamlit run app.py --server.port=8501 --server.enableXsrfProtection=false --server.enableCORS=false"]
