FROM cgr.dev/chainguard/python:latest-dev AS dev

ENV PATH="/tmp/venv/bin:$PATH"
COPY requirements.txt requirements.txt
RUN python -m venv /tmp/venv && pip install -r requirements.txt

FROM cgr.dev/chainguard/python:latest

WORKDIR /app

COPY main.py main.py
COPY --from=dev /tmp/venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

ENTRYPOINT ["python", "main.py"]
