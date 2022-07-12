import json
from .service import Question, Answer, save_questions


OPEN_TRIVIA_URL = 'https://opentdb.com/api.php?amount=10'


def handler(event, context):
    print('received event:')
    print(event)

    # Pull 10 Questions from OpenTrivia

    # Transform them to Question Format

    # Save them to Question DB



    return True