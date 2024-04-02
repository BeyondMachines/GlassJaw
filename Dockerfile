FROM python:3.7-alpine

RUN mkdir /app
RUN apk --update add bash nano g++

ENV vulnerable=1
ENV tokentimetolive=60

ENV MY_NAME="Docker User" APP_VERSION="1.0"

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

# ENTRYPOINT ["python"]
# CMD ["app.py"]
CMD echo "Hello, ${MY_NAME}. You are running version ${APP_VERSION} of the application."