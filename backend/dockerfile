FROM python:3.9

RUN apt-get update

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

EXPOSE 8000
