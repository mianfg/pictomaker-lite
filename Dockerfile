# Pull base image
FROM python:3.10 as builder
# Set environment variables
COPY requirements.txt requirements.txt

# Install pipenv
RUN set -ex && pip install --upgrade pip

# Install dependencies
RUN set -ex && pip install -r requirements.txt
RUN set -ex && python -m spacy download es_core_news_sm 
RUN set -ex && python -m spacy download en_core_web_sm 
RUN set -ex && python -m spacy download pl_core_news_sm 

FROM builder as final
WORKDIR /api
COPY . /api
