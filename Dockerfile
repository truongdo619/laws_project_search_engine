FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN apt-get update && apt-get install -y wkhtmltopdf xvfb
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
