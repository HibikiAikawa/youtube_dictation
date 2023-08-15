FROM python:3.10.10-bullseye

EXPOSE 8000

ENV PATH /root/.local/bin:$PATH

RUN apt-get update \
    && apt-get install curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create true

WORKDIR /work

COPY pyproject.toml /work

RUN poetry install --no-root

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]