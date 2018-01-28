import os
from datetime import datetime
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_index():    
    response = app.response_class(
        response='{"message": "welcome to api-examples"}',
        status=200,
        mimetype='application/json'
    )

    return response

@app.route("/hello", methods=["GET"])
def get_hello():    
    response = app.response_class(
        response='{"message": "Hello World"}',
        status=200,
        mimetype='application/json'
    )

    return response

@app.route("/datetime", methods=["GET"])
def get_datetime():
    now = str(datetime.now())
    #print(now)

    response = app.response_class(
        response='{"datetime": "' + now + '"}',
        status=200,
        mimetype='application/json'
    )

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    