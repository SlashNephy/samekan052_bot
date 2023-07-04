FROM python:3.11.4-slim-bullseye@sha256:87a1f4d072ca88161bcd57878d912cae21eb718d9608859f57654ca05ab58545

ARG BUILD_DEPENDENCIES="build-essential"

COPY ./requirements.txt /tmp/requirements.txt

RUN apt update \
    && apt install -y --no-install-recommends $BUILD_DEPENDENCIES \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    \
    # pip
    && cd /tmp \
    && python -m pip install --upgrade pip \
    && pip install --no-cache-dir \
        -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt \
    \
    ## Cleanup
    && apt purge -y $BUILD_DEPENDENCIES \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists

WORKDIR /
COPY ./samekan052.py /app.py
ENTRYPOINT ["python", "-u", "/app.py"]
