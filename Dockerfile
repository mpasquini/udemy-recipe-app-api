FROM python:3.7-alpine

MAINTAINER Matteo Pasquini

ENV PYTHONUBUFFERED=1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip \
    && apk add --update --no-cache postgresql-client jpeg-dev \
    && apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev \
    && pip install -r /requirements.txt \
    && apk del .tmp-build-deps

RUN mkdir -p /app
WORKDIR /app
COPY ./app /app
RUN adduser -D user \
    && mkdir -p /vol/web/media \
    && mkdir -p /vol/web/static \
    && chown -R user:user /vol/ \
    && chmod -R 755 /vol/web
USER user


