FROM python:2.7-alpine
MAINTAINER Fahad Hayat <fahadhayat@outlook.com>

ENV INSTALL_PATH /server
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "server.app:create_app()"