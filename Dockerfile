From python:3.8.6
MAINTAINER lyj "liyuanjin@csvw.com"

RUN apt-get update && \
    apt-get install -y openssh-server && \
    apt-get install -y vim

RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config  && mkdir /run/sshd

RUN echo "root:f123456" | chpasswd

RUN pip install flask pyserial

COPY . /root
WORKDIR /root
USER root

EXPOSE 22
EXPOSE 5200

CMD /usr/sbin/sshd -D
