FROM python:3.11

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
COPY pipeline.py pipeline.py

ENTRYPOINT ["python", "pipeline.py"]