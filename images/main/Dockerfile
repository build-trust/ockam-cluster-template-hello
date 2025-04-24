FROM cgr.dev/chainguard/python:latest-dev AS dev

WORKDIR /app

RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"
COPY wheels/ /app/wheels/
RUN arch=$(uname -m) && \
    if [ "$arch" = "aarch64" ]; then \
    pip install /app/wheels/ockam-0.1.0-cp312-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl; \
    else \
    pip install /app/wheels/ockam-0.1.0-cp312-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl; \
    fi

FROM cgr.dev/chainguard/python:latest

WORKDIR /app

COPY main.py main.py
COPY --from=dev /app/venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

ENTRYPOINT ["python", "main.py"]
