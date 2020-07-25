#FROM ubuntu:18.04
FROM python:3.7-alpine
ARG S3_BUCKET_NAME
ARG S3_ACCESS_KEY
ARG S3_SECRET_ACCESS_KEY
ENV S3_BUCKET_NAME=$S3_BUCKET_NAME
ENV S3_ACCESS_KEY=$S3_ACCESS_KEY
ENV S3_SECRET_ACCESS_KEY=$S3_SECRET_ACCESS_KEY
#RUN apt-get update \
#    && apt-get install -y  python3 \
#    python3-pip
COPY application /application
WORKDIR /application
RUN pip3 install -r requirements.txt
CMD [ "gunicorn","--bind", "0.0.0.0:8000" ,"app:app" ]
EXPOSE 8000