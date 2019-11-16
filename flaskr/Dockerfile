FROM python:3.6-slim

RUN pip3 install --no-cache-dir flask keras tensorflow && \
    mkdir src

COPY src src
COPY fruitModel.h5 /

EXPOSE 5000

ENTRYPOINT export ENV=prod && python3 src/main.py