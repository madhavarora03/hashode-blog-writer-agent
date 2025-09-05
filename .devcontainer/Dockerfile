FROM mcr.microsoft.com/devcontainers/python:3.10

ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y curl

RUN pip install --upgrade pip