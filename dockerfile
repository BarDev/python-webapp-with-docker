FROM python:alpine

WORKDIR /api

RUN apk update
    
RUN pip install flask

COPY . .

CMD [ "python", "./hello-world-api.py" ]