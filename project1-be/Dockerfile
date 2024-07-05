FROM python:3.11-slim as builder
# Install Poetry
RUN pip3 install poetry==1.8.2
WORKDIR /app
COPY pyproject.toml poetry.lock /app
# virtual env is created in "/app/.venv" directory

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Install dependencies

# For MySQL
RUN apt -y update && \
    apt-get install -y \
        python3-dev \
        default-libmysqlclient-dev \
        build-essential \
        pkg-config

RUN --mount=type=cache,target=/tmp/poetry_cache poetry install --only main --no-root
RUN poetry install

FROM python:3.11-slim as app

# For MySQL (should not be repeated like this, TODO)
RUN apt -y update && \
    apt-get install -y \
        python3-dev \
        default-libmysqlclient-dev \
        build-essential \
        pkg-config
COPY src /app/src
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
# ENTRYPOINT ["ls", "/app/src/", "-a"]
# ENTRYPOINT ["/app/.venv/bin/python", "/app/src/manage.py", "runserver", "0.0.0.0:7665"]
ENTRYPOINT ["/app/src/project1_be/entrypoints/app.sh"]

FROM python:3.11-slim as worker

# For MySQL (should not be repeated like this, TODO)
RUN apt -y update && \
    apt-get install -y \
        python3-dev \
        default-libmysqlclient-dev \
        build-essential \
        pkg-config

COPY src /app/src
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# TODO: string "project1_be" should be gotten from somewhere
ENTRYPOINT ["/app/src/project1_be/celery-entrypoint.sh"]
# ENTRYPOINT ["/app/.venv/bin/celery", "-A", "project1_be", "worker"]
