FROM python:3.11-slim

# inside container
WORKDIR /app

# copy the app code, from wherever
COPY app/ .  

RUN pip install --upgrade pip &&\ 
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
