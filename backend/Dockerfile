FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry
RUN mkdir -p /app

COPY poetry.lock .
COPY pyproject.toml .


RUN poetry install --without dev

COPY . .

CMD ["poetry", "run", "uvicorn", "source.main:app", "--host=0.0.0.0", "--port=8000", "--reload"]