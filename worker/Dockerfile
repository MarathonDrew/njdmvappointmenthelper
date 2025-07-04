FROM python:3

WORKDIR /app

RUN pip install --no-cache-dir requests 

COPY . /app

CMD ["python", "check.py"]
