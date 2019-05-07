FROM frolvlad/alpine-python3


ENV PYTHONUNBUFFERED 1
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN mkdir /wirecard-challenge
WORKDIR /wirecard-challenge

ADD . /wirecard-challenge

# Installing project dependencies.
RUN pip install -U pip
RUN pip install -r requirements.txt

