FROM python:3-bullseye

ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 0
ENV COLUMNS 80

RUN apt-get update \
 && apt-get install -y \
 nano python3-pip gettext chrpath libssl-dev libxft-dev \
 libfreetype6 libfreetype6-dev  libfontconfig1 libfontconfig1-dev

WORKDIR /code/

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/
COPY --chmod=0600 .pg* /root/
