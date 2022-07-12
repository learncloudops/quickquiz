from typing import List, Optional, Dict
from service import Question, Answer, save_questions


OPEN_TRIVIA_URL = 'https://opentdb.com/api.php?amount=10'


def handler(event, context):
    print('received event:')
    print(event)
    # Pull 10 Questions from OpenTrivia
    # Transform them to Question Format
    # Save them to Question DB

    q: List[Question] = []
    q.append(
        Question(question_text='Am I good?', question_type='boolean', category='Entertainment', difficulty='easy',
                answers=[Answer(index=0, answer_text='Yes', is_correct=True), 
                        Answer(index=1, answer_text='No', is_correct=False)]))
    q.append(
        Question(question_text='Am I smart?', question_type='boolean', category='Entertainment', difficulty='easy',
                answers=[Answer(index=0, answer_text='Yes', is_correct=True),
                            Answer(index=1, answer_text='No', is_correct=False)]))
    q.append(
        Question(question_text='Am I dead sexy?', question_type='boolean', category='Entertainment', difficulty='easy',
                answers=[Answer(index=0, answer_text='Yes', is_correct=True),
                            Answer(index=1, answer_text='No', is_correct=False)]))
    q.append(
        Question(question_text='Am I a moron?', question_type='boolean', category='Entertainment', difficulty='easy',
                answers=[Answer(index=0, answer_text='Yes', is_correct=True),
                            Answer(index=1, answer_text='No', is_correct=False)]))
    q.append(
        Question(question_text='Am I hideous?', question_type='boolean', category='Entertainment', difficulty='easy',
                answers=[Answer(index=0, answer_text='Yes', is_correct=True),
                            Answer(index=1, answer_text='No', is_correct=False)]))
    q.append(
        Question(question_text='Am I a tech badass?', question_type='boolean', category='Entertainment', difficulty='easy',
                answers=[Answer(index=0, answer_text='Yes', is_correct=True),
                            Answer(index=1, answer_text='No', is_correct=False)]))
    q.append(
        Question(question_text='Am I gravitationally challenged?', question_type='boolean', category='Entertainment', difficulty='easy',
                answers=[Answer(index=0, answer_text='Yes', is_correct=True),
                            Answer(index=1, answer_text='No', is_correct=False)]))
    q.append(
        Question(question_text='Am I done?', question_type='boolean', category='Entertainment', difficulty='easy',
                answers=[Answer(index=0, answer_text='Yes', is_correct=True),
                            Answer(index=1, answer_text='No', is_correct=False)]))
    save_questions(questions=q)


    return True


if __name__ == '__main__':
    handler({},{})