FROM python:alpine

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

WORKDIR /
COPY ./samekan052.py /app.py
ENTRYPOINT ["python", "-u", "/app.py"]
