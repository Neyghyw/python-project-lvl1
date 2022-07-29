import random


RULES = 'What is the result of the expression?'


def get_calc_question_and_answer() -> (str, str):
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)
    operator = random.choice("+-*")
    question = f'{operand1} {operator} {operand2}'
    answer = str(eval(question))
    return question, answer
