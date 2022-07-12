import os
import random
from typing import Dict, List
import boto3
from boto3.dynamodb.conditions import Key, Attr


DB_TABLE = os.environ.get('STORAGE_QUESTIONDB_NAME', 'questiondb-main')
table = boto3.resource('dynamodb').Table(DB_TABLE)


def get_question_sequence():
    result = table.query(
        KeyConditionExpression=Key('pk').eq('QSEQ')
    )
    items = result['Items']
    result = {}

    if result.get('Count') > 0:
      seq = items[0]
      result = {
        'name': 'question_sequence',
        'sequence': seq.get('value'),
        'last_mod': seq.get('mod_timest')
      }
    else:
      raise ValueError('Could not find the question sequence. Something went wrong!')

    return result


def random_questions(max_seq: int):
  rand_nums = []
  if max_seq < 5:
    raise ValueError(
        'there are not 5 questions available to parse into a game')
  else:
    for x in range(5):
      rand_nums.append(random.randrange(1, max_seq))
  
  return rand_nums




def handler(event, context):
  '''
    TODO Implement Me

    Generates a game of 5 questions using random numbers
    between 1 and the sequence max.

    How it works:

      * Gets the question sequence from the question api
      * Generates random numbers between 1 and the sequence
      * Saves the new game
  '''
  print('received event:')
  print(event)

  # read out the question sequence
  # sequence: Dict = get_question_sequence()

  # get 5 random questions
  #random_questions: List = random_questions(sequence.get('sequence', 0))

  # save the game
  game = {}

  
  return True