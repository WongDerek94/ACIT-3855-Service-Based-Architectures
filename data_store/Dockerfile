FROM ubuntu:16.04

MAINTAINER Derek Wong "dwong393@my.bcit.ca"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

RUN python3 /app/create_tables_mysql.py

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]