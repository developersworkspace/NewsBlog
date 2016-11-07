FROM ubuntu:16.04
MAINTAINER Barend Erasmus developersworkspace@gmail.com
RUN apt-get update
RUN apt-get -y install build-essential libssl-dev libffi-dev python-dev git python3 python3-pip
RUN pip3 install pymysql beautifulsoup4 requests
RUN git clone https://github.com/developersworkspace/NewsBlog.git /repo
WORKDIR /repo/web
ENTRYPOINT ["/usr/bin/python3", "db_exchange_rate_processor.py"]