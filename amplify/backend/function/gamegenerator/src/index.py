from typing import List
from service import (create_game, current_date_format, 
                     random_questions)


def handler(event, context):
  '''
    TODO Implement Me Better

    Generates a game of 5 questions using random numbers
    between 1 and question_sequence.

    How it works:

      * Generates random numbers between 1 and the sequence in the event
      * Saves the new game

    This is actually broken. Rather than being on a CRON, it should 
    react to questions being written to the questiondb and auto-generating.

    Questions Load -> Game gets generated

  '''
  print('received event:')
  print(event)

  dtstr: str = current_date_format()
  sequence: int = event.get('question_sequence', 500)
  if not sequence or sequence == 0:
    raise ValueError('cannot process this sequence. dying')
  else:
    questions: List[int] = random_questions(sequence)
    create_game(dtstr, questions)
  
  return True



if __name__ == '__main__':
  handler({
    'question_sequence': 16
  },{})