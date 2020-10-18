FROM python:3.8.5

ENV PYTHONUNBUFFERED 1

RUN mkdir /MovieBlog
WORKDIR /MovieBlog

ADD requirements.txt /MovieBlog/
RUN pip install -r requirements.txt

ADD . /MovieBlog/

