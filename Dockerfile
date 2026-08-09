FROM ghcr.io/astral-sh/uv:python3.13-alpine

COPY ./uv.lock ./pyproject.toml /app/

WORKDIR /app

RUN uv sync --frozen --no-install-project --no-dev

COPY . /app/

CMD ["uv", "run", "main.py"]
