FROM python:3.7-alpine
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
RUN mkdir /app
COPY ./src/* /app
RUN  ls -la /app
WORKDIR /app
