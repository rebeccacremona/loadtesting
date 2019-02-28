FROM python:3.6-stretch

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y jq

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
