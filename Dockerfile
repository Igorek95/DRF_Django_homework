FROM python:3

WORKDIR /drf_api

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .