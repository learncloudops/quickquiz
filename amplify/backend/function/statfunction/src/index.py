from typing import Dict
from flask_cors import CORS
from flask import Flask, jsonify, request
import awsgi
from boto3.dynamodb.conditions import Key, Attr
import boto3
import os

app = Flask(__name__)
cors = CORS(app)
DB_TABLE = os.environ.get('STORAGE_STATSDB_NAME', 'statsdb-main')
table = boto3.resource('dynamodb').Table(DB_TABLE)


@app.route('/', methods=['GET'])
def index():
    return jsonify(message='sup fool!')


def handler(event, context):
    '''
    Translates the Flask goodness into
    the ApiGateway/Lambda paradigm
    '''
    return awsgi.response(app, event, context)


if __name__ == '__main__':
    app.run(debug=True)
