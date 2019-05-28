FROM python:3.7.3-slim-stretch

ADD . /app
WORKDIR /app

CMD ["python", "source.py"]
