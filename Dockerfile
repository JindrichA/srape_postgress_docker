# syntax=docker/dockerfile:1
FROM python:3.10-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apk update
RUN apk add chromium
RUN apk add chromium-chromedriver
RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
# Doresit variantu s chrome driverem
#CMD cd sreality_scrape/sreality_scrape/  && scrapy crawl myspider  && cd -&& flask run --host=0.0.0.0
CMD  flask run --host=0.0.0.0