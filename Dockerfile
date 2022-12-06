FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
COPY requirements.dev.txt .
RUN pip install -r requirements.dev.txt
COPY . .
RUN python create_tables.py
RUN python load_fixtures.py

ENTRYPOINT ["sh", "entrypoint.sh"]