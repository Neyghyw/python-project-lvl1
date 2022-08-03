import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
RANGE_START = 1
RANGE_END = 100


def get_question_and_answer() -> (str, str):
    question = random.randint(RANGE_START, RANGE_END)
    answer = (question % 2 == 0 and 'yes') or 'no'
    return str(question), answer
