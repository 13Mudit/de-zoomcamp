FROM python:3.11

RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
COPY pipeline.py pipeline.py

ENTRYPOINT ["python", "pipeline.py"]