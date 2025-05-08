FROM ghcr.io/build-trust/ockam-python-dev:latest AS dev

ENV PATH="/tmp/venv/bin:$PATH"
COPY requirements.txt requirements.txt
RUN python -m venv /tmp/venv && pip install -r requirements.txt

FROM ghcr.io/build-trust/ockam-python:latest

WORKDIR /app

COPY main.py main.py
COPY --from=dev /tmp/venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

ENTRYPOINT ["python", "main.py"]
