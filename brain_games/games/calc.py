import random


DESCRIPTION = 'What is the result of the expression?'
RANGE_START = 1
RANGE_END = 100


def get_arithmetic_expression_result(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2


def get_question_and_answer() -> (str, str):
    operand1 = random.randint(RANGE_START, RANGE_END)
    operand2 = random.randint(RANGE_START, RANGE_END)
    operator = random.choice('+-*')
    question = f'{operand1} {operator} {operand2}'
    answer = get_arithmetic_expression_result(operand1, operand2, operator)
    return question, str(answer)
