FROM ubuntu

# Lkernel Continuous integration

LABEL version="v1.0"

RUN apt update
RUN apt install -y lua5.3

COPY ./ /pykernel

WORKDIR /pykernel