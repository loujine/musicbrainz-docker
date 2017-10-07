FROM debian:stretch
MAINTAINER loujine <loujine@protonmail.com>

USER root
ENV DEBIAN_FRONTEND noninteractive
ENV REPO http://httpredir.debian.org
RUN echo "deb $REPO/debian stretch main" > /etc/apt/sources.list \
 && echo "deb $REPO/debian stretch-updates main" >> /etc/apt/sources.list \
 && echo "deb $REPO/debian stretch-proposed-updates main" >> /etc/apt/sources.list \
 && echo "deb http://security.debian.org stretch/updates main" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get upgrade -y
RUN apt-get install -y --no-install-recommends supervisor python-pip python-setuptools python3-pip python3-setuptools python-wheel python3-wheel
RUN apt-get install -y --no-install-recommends jupyter-notebook jupyter-nbextension-jupyter-js-widgets
RUN apt-get install -y --no-install-recommends python3-notebook python3-pandas python3-requests python3-sqlalchemy python3-psycopg2 python3-matplotlib
RUN apt-get install -y --no-install-recommends python-notebook python-pandas python-requests python-sqlalchemy python-psycopg2 python-matplotlib
RUN apt-get install -y --no-install-recommends wget bzip2
RUN apt-get install -y --no-install-recommends procps vim-common # for debug
RUN pip3 install version_information
RUN pip install version_information
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN pip3 install plotly --upgrade
RUN pip install plotly --upgrade
RUN pip3 install ipyleaflet
RUN jupyter nbextension enable --py --sys-prefix ipyleaflet
RUN pip install plotly --upgrade
ENV NB_USER jovyan
RUN useradd -g 100 -m -s /bin/bash $NB_USER

USER $NB_USER
WORKDIR /home/$NB_USER/
RUN mkdir -p notebooks js
RUN ipython3 profile create
COPY helper.py .ipython/profile_default/startup/helper.py
COPY plotly_env.py .ipython/profile_default/startup/plotly_env.py
RUN wget https://bitbucket.org/loujine/musicbrainz-dataviz/get/master.tar.bz2 \
 && tar xfj /home/$NB_USER/master.tar.bz2
RUN mv loujine-musicbrainz-dataviz-* dataviz-examples
WORKDIR /home/$NB_USER/js/

USER root
EXPOSE 8888
CMD ["/usr/bin/supervisord"]
