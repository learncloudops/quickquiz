from typing import Dict
from flask_cors import CORS
from flask import Flask, jsonify, request
import awsgi
from boto3.dynamodb.conditions import Key, Attr
import boto3
import os

app = Flask(__name__)
cors = CORS(app)
DB_TABLE = os.environ.get('STORAGE_QUESTIONDB_NAME', 'questiondb-main')
table = boto3.resource('dynamodb').Table(DB_TABLE)


@app.route('/', methods=['GET'])
def index():
    return jsonify(message='sup fool!')


@app.route('/questions/sequence', methods=['GET'])
def get_sequence():
    result = table.query(
        KeyConditionExpression=Key('pk').eq('QSEQ')
    )
    items = result['Items']
    if result.get('Count') > 0:

        seq = items[0]
        return jsonify(data={ 
            'name': 'question_sequence',
            'sequence': seq.get('value'),
            'last_mod': seq.get('mod_timest')
        })
    else:
        return jsonify(message='Sequence not found'), 404


def handler(event, context):
    '''
    Translates the Flask goodness into
    the ApiGateway/Lambda paradigm
    '''
    return awsgi.response(app, event, context)


if __name__ == '__main__':
    app.run(debug=True)
