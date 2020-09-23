FROM python:3.8-slim-buster

RUN apt-get update \
&& apt-get install curl -y \
&& apt-get clean

ADD .bashrc /root/

COPY requirements.txt /app/requirements.txt

COPY app.py /app/app.py

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD python ./app.py
