FROM ubuntu:16.04
MAINTAINER Barend Erasmus developersworkspace@gmail.com
RUN apt-get update
RUN apt-get -y install build-essential libssl-dev libffi-dev python-dev git python3 python3-pip
RUN pip3 install Flask gunicorn pymysql
RUN git clone https://github.com/developersworkspace/NewsBlog.git /repo
WORKDIR /repo/web
ENTRYPOINT ["/usr/local/bin/gunicorn", "-b", ":8080", "runserver:app"]