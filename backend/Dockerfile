# Docker for Back End
FROM python:3.5-alpine
MAINTAINER Fahad Hayat <fahadhayat@outlook.com>

ENV INSTALL_PATH_SERVER /backend
RUN mkdir -p $INSTALL_PATH_SERVER

WORKDIR $INSTALL_PATH_SERVER

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


CMD gunicorn -b 0.0.0.0:5000 --access-logfile - "backend.app:create_app()"