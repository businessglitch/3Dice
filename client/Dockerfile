# Docker for Front End
FROM node:alpine as build
MAINTAINER Fahad Hayat <fahadhayat@outlook.com>

ENV INSTALL_PATH_CLIENT /client
RUN mkdir -p $INSTALL_PATH_CLIENT
WORKDIR $INSTALL_PATH_CLIENT

COPY package.json package.json

RUN npm install

COPY . .
EXPOSE 3000
RUN npm start