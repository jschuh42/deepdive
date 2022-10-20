FROM python:3.7-alpine

RUN mkdir /app
ADD . /app

WORKDIR /app

RUN pip3 install -r requirements.txt \
    pip install -e .

ENV FLASK_APP=flaskr
ENV FLASK_ENV=development

CMD flask init-db ; flask --app flaskr --debug run --host=0.0.0.0 -p 5000
