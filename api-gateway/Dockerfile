FROM python:3.11

WORKDIR /app

COPY . /app

ENV PYTHONPATH=/app/src

RUN pip install -r src/requirements.txt

CMD ["python", "src/app.py"]
