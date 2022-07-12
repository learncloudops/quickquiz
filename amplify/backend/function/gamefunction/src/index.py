from typing import Dict
from flask_cors import CORS
from flask import Flask, jsonify, request
import awsgi
from boto3.dynamodb.conditions import Key, Attr
import boto3
import os

app = Flask(__name__)
cors = CORS(app)
DB_TABLE = os.environ.get('STORAGE_GAMEDB_NAME', 'gamedb-main')
table = boto3.resource('dynamodb').Table(DB_TABLE)


@app.route('/', methods=['GET'])
def index():
    return jsonify(message='sup fool!')


@app.route('/user/<username>')
def profile(username):
    return jsonify(message=f'Hello {username}')


@app.route('/games/played/user/<string:username>', methods=['GET'])
def get_played_games_by_user(username: str):
    result = table.query(
        IndexName='sortIndex',
        KeyConditionExpression=Key('sk').eq(username),
        Limit=10
    )
    data = []
    for item in result.get('Items'):
        item['data']['score'] = int(item['data']['score'])
        data.append(item['data'])
    print(data)

    return jsonify(data=data)


@app.route('/games/played', methods=['POST','PUT'])
def save_played_game():
    # TODO prevent the user from sending the same game twice
    msg = request.get_json()
    item = { 
        'pk': msg.get('date_played'),
        'sk': msg.get('username'),
        'data': {            
            'complete': msg.get('complete'),
            'date_played': msg.get('date_played'),
            'username': msg.get('username'),
            'score': msg.get('score'),
            'correct': msg.get('correct')
        }
    }
    table.put_item(Item=item)
    return jsonify(message="Game Saved")


def handler(event, context):
    '''
    Translates the Flask goodness into
    the ApiGateway/Lambda paradigm
    '''
    return awsgi.response(app, event, context)


if __name__ =='__main__':
    app.run(debug=True)