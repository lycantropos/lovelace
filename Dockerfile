FROM python:3

COPY . /lovelace/
WORKDIR /lovelace/

RUN python3 -m pip install .
