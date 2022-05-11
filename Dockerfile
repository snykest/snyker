FROM python:3.10-slim-bullseye

RUN mkdir /project
WORKDIR /project
RUN pip install poetry
COPY pyproject.toml poetry.lock .
RUN poetry install
COPY . .
RUN poetry run pytest
