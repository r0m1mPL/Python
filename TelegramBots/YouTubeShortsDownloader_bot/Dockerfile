FROM python:3

WORKDIR /app

COPY . .

RUN pip install -U pip setuptools wheel

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
