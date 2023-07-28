FROM python:3.11.4-slim-bullseye@sha256:52c7a54aa5e5068ce76edaf3f8652a64fb99e378fb89fb0bfbe21a8756d0013c

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
