FROM python:3.11-slim

# inside container
WORKDIR /app

# context is root, need requirement file
COPY ./app .
COPY docker/streamlit/requirements.txt .  

RUN pip install --upgrade pip &&\ 
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.baseUrlPath", "/app"]
