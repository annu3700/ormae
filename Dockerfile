From centos:7

MAINTAINER kapilbk1996@gmail.com

# Install Python and its depedencies
RUN yum install -y python3 \
 &&	pip3 install requests \
 && pip3 install pymongo

# Install MongoDB
RUN yum -y install wget git \
 && wget http://downloads.mongodb.org/linux/mongodb-linux-x86_64-3.2.22.tgz \
 && tar -zxvf /mongodb-linux-x86_64-3.2.22.tgz \
 && rm -f /mongodb-linux-x86_64-3.2.22.tgz \
 && mkdir -p /data/db \
 && yum clean all

RUN git clone https://github.com/tomasbasham/ratelimit \
 && cd ratelimit \
 && python3 setup.py install
 
ENV PATH=$PATH:"/mongodb-linux-x86_64-3.2.22/bin"

COPY assignment.py /
COPY startUpScript.sh /

RUN chown root /startUpScript.sh \
 && chgrp root /startUpScript.sh \
 && chmod 777 /startUpScript.sh 

CMD ["/bin/bash","-c","/startUpScript.sh && tail -f /dev/null"]
