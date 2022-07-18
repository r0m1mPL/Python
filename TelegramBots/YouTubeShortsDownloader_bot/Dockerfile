FROM python:3-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip setuptools wheel

RUN pip install -r requirements.txt

COPY . .
