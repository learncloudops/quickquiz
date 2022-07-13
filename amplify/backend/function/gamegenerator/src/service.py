import os
import random
import boto3
from boto3.dynamodb.conditions import Key, Attr
from typing import Dict, List
from datetime import datetime


DB_TABLE = os.environ.get('STORAGE_GAMEDB_NAME', 'gamedb-main')
table = boto3.resource('dynamodb').Table(DB_TABLE)
DATE_FORMAT = "%Y%m%d"
TIMEST_FORMAT = "%Y%m%dT%H%M%S"

def current_date_format():
  curr_dtm = datetime.now()
  return curr_dtm.strftime(DATE_FORMAT)


def current_timest():
  curr_dtm = datetime.now()
  return curr_dtm.strftime(TIMEST_FORMAT)
  

def random_questions(max_seq: int):
  rand_nums = []
  if max_seq < 5:
    raise ValueError(
        'there are not 5 questions available to parse into a game')
  else:
    for x in range(5):
      rand_nums.append(random.randrange(0, max_seq))

  return rand_nums


def create_game(date_str: str, q_ids: List[int]):
  item: Dict = {
    'pk': date_str,
    'sk': 'Game',
    'data': {
      'questions': q_ids
    },
    'mod_timest': current_timest()
  }
  table.put_item(Item=item)
