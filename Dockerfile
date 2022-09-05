FROM python:3.7-alpine

RUN mkdir /app

WORKDIR /app

ADD requirements.txt /app
ADD * /app

RUN pip3 install -r requirements.txt

ENV FLASK_APP=app
ENV FLASK_ENV=production

CMD flask run --host=0.0.0.0 -p 5000
