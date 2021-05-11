FROM python:3.9

LABEL maintainer="Marlon Leite"
LABEL description="Credit Recovery"

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y install \
    python-pip \
    libpq-dev \
    postgresql-contrib
RUN pip install --upgrade pip
RUN pip install psycopg2-binary

RUN mkdir /code

WORKDIR /code

ADD . /code/

RUN pip install --upgrade pip
RUN pip install -r requirements-dev.txt

EXPOSE 8000
