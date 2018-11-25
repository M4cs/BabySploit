FROM ubuntu:latest
MAINTAINER Furkan SAYIM <furkan.sayim@yandex.com>

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install git -y \
    && apt-get install python3 -y  \
    && apt-get install wget -y \
    && apt-get install python3-pip -y \
    && apt-get install software-properties-common -y

RUN apt-get update \
    && apt-get install exploitdb netcat nmap perl -y \
    && apt-get autoremove -y \
    && ln -s -f /usr/share/zoneinfo/Etc/GMT+3 /etc/localtime \
    && apt-get -y install php7.0 \
    && pip3 install babysploit
    
RUN mkdir /BabySploit

RUN babysploit

WORKDIR /BabySploit
