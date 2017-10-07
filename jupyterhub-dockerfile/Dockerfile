FROM debian:buster
MAINTAINER loujine <loujine@protonmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV REPO=http://cdn-fastly.deb.debian.org
RUN echo "deb $REPO/debian buster main" > /etc/apt/sources.list
RUN apt-get -y update
RUN apt-get install -y apt-utils
RUN apt-get -y upgrade
RUN apt-get -y install wget git bzip2 gpg gpg-agent
RUN apt-get -y install locales
RUN /usr/sbin/update-locale LANG=C.UTF-8
RUN locale-gen C.UTF-8
ENV LANG C.UTF-8

RUN apt-get -y update
# Python2.7
RUN apt install -y --no-install-recommends python-notebook
RUN apt install -y --no-install-recommends python2.7
RUN apt install -y --no-install-recommends python-pip python-setuptools python-wheel
RUN apt install -y --no-install-recommends python-sqlalchemy python-psycopg2 python-jinja2 python-requests python-lxml python-html5lib python-bs4
RUN apt install -y --no-install-recommends python-pandas python-matplotlib

# Python3.5
RUN apt install -y --no-install-recommends python3-notebook
RUN apt install -y --no-install-recommends python3.5
RUN apt install -y --no-install-recommends python3-pip python3-setuptools python3-wheel
RUN apt install -y --no-install-recommends python3-sqlalchemy python3-psycopg2 python3-jinja2 python3-requests python3-lxml python3-html5lib python3-bs4
RUN apt install -y --no-install-recommends python3-pandas python3-matplotlib
RUN apt install -y --no-install-recommends jupyter-core jupyter-notebook
# RUN apt install -y --no-install-recommends jupyter-nbextension-jupyter-js-widgets

# NodeJS
RUN echo "deb https://deb.nodesource.com/node_6.x buster main" >> /etc/apt/sources.list
RUN wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -
RUN apt-get -y update
RUN apt install -y --no-install-recommends nodejs npm

# Notebook widgets
RUN pip install version_information
RUN pip3 install version_information

# lastest plotly
RUN pip install plotly --upgrade
RUN pip3 install plotly --upgrade

# Install latest jupyterhub
RUN pip3 install -U jupyterhub
RUN npm install -g configurable-http-proxy

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf ~/.cache ~/.npm

RUN mkdir -p /srv/jupyterhub/
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

ENV NB_USER loujine
RUN useradd -g 100 -m -p $(openssl passwd -1 $NB_USER) -s /bin/bash $NB_USER

USER $NB_USER
WORKDIR /home/$NB_USER/
RUN ipython3 profile create

USER root
WORKDIR /srv/jupyterhub/
EXPOSE 8000

CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
