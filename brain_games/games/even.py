import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer() -> (str, str):
    question = random.randint(1, 100)
    answer = (question % 2 == 0 and "yes") or "no"
    return str(question), answer
