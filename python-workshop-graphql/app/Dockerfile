FROM ubuntu:latest

#Autor
MAINTAINER Hugo Barzano Cruz <hugobarzano@gmail.com>

ENV PYTHONUNBUFFERED 1

RUN \
    apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    ca-certificates \
    gcc \
    git \
    libpq-dev \
    make \
    python-pip \
    python2.7 \
    python2.7-dev \
    ssh \
    mongodb \
    && apt-get autoremove \
    && apt-get clean

RUN sed -i 's/^bind_ip = 127.0.0.1/\#bind_ip = 0.0.0.0/g' /etc/mongodb.conf
RUN service mongodb restart

ADD ./ /opt
RUN pip install -r /opt/requirements.txt

EXPOSE 27017
EXPOSE 8080
RUN chmod +x /opt/executor.sh

CMD /opt/executor.sh
