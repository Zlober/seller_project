FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
COPY ozon-0.1.0-py3-none-any.whl /app
RUN pip install poetry
RUN poetry install