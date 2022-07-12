from typing import List, Optional, Dict
from dataclasses import dataclass, asdict
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import boto3
import os
from datetime import datetime

DB_TABLE = os.environ.get('STORAGE_QUESTIONDB_NAME', 'questiondb-main')
table = boto3.resource('dynamodb').Table(DB_TABLE)

DATE_FORMAT = "%Y%m%dT%H%M%S"


@dataclass
class Answer:
  index: int
  answer_text: str
  is_correct: bool


@dataclass
class Question:
  question_text: str
  question_type: str
  category: str
  difficulty: str
  answers: List[Answer]
  question_id: Optional[int]=0


def current_date_format():
  curr_dtm = datetime.now()
  return curr_dtm.strftime(DATE_FORMAT)



def get_question_sequence() -> int:
  '''
    Gets the current question sequence.
  '''
  result = table.query(
      KeyConditionExpression=Key('pk').eq('QSEQ')
  )
  items = result.get('Items',[])
  if result.get('Count') > 0:
    seq = items[0]
    return seq.get('value')
  else:
    raise ValueError(
        'Could not find the question sequence. Something went wrong!')


def update_question_sequence(new_value: int) -> None:
  table.put_item(Item={
    'pk':'QSEQ',
    'value': int(new_value),
  })


def transform_to_db_item(q: Question) -> Dict:
  return {
    'pk': str(q.question_id),
    'sk': 'Question',
    'mod_timest': current_date_format(),
    'data': {
      'q_id': int(q.question_id),
      'q_type': q.question_type,
      'q_category': q.category,
      'q_difficult': q.difficulty,
      'answers': [asdict(a) for a in q.answers ]
    }
  }



def save_questions(questions: List[Question]) -> bool:
  seq: int = get_question_sequence()

  try:
    for question in questions:
      question.question_id = seq
      table.put_item(Item=transform_to_db_item(question))
      seq = seq + 1
  except ClientError:
    print('failed to save items')
    raise

  update_question_sequence(seq)


# if __name__ == '__main__':
#   q: List[Question] = []
#   q.append(
#     Question(question_text='Am I good?', question_type='boolean', category='Entertainment', difficulty='easy',
#              answers=[Answer(index=0, answer_text='Yes', is_correct=True), 
#                       Answer(index=1, answer_text='No', is_correct=False)]))
#   q.append(
#       Question(question_text='Am I smart?', question_type='boolean', category='Entertainment', difficulty='easy',
#                answers=[Answer(index=0, answer_text='Yes', is_correct=True),
#                         Answer(index=1, answer_text='No', is_correct=False)]))
#   q.append(
#       Question(question_text='Am I dead sexy?', question_type='boolean', category='Entertainment', difficulty='easy',
#                answers=[Answer(index=0, answer_text='Yes', is_correct=True),
#                         Answer(index=1, answer_text='No', is_correct=False)]))
#   q.append(
#       Question(question_text='Am I a moron?', question_type='boolean', category='Entertainment', difficulty='easy',
#                answers=[Answer(index=0, answer_text='Yes', is_correct=True),
#                         Answer(index=1, answer_text='No', is_correct=False)]))
#   q.append(
#       Question(question_text='Am I hideous?', question_type='boolean', category='Entertainment', difficulty='easy',
#                answers=[Answer(index=0, answer_text='Yes', is_correct=True),
#                         Answer(index=1, answer_text='No', is_correct=False)]))
#   q.append(
#       Question(question_text='Am I a tech badass?', question_type='boolean', category='Entertainment', difficulty='easy',
#                answers=[Answer(index=0, answer_text='Yes', is_correct=True),
#                         Answer(index=1, answer_text='No', is_correct=False)]))
#   q.append(
#       Question(question_text='Am I gravitationally challenged?', question_type='boolean', category='Entertainment', difficulty='easy',
#                answers=[Answer(index=0, answer_text='Yes', is_correct=True),
#                         Answer(index=1, answer_text='No', is_correct=False)]))
#   q.append(
#       Question(question_text='Am I done?', question_type='boolean', category='Entertainment', difficulty='easy',
#                answers=[Answer(index=0, answer_text='Yes', is_correct=True),
#                         Answer(index=1, answer_text='No', is_correct=False)]))
#   save_questions(questions=q)