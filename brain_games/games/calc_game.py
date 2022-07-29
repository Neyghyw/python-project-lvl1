import random


RULES = 'What is the result of the expression?'


def get_arithmetic_expression_result(operand1, operand2, operator):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    else:
        return operand1 * operand2


def get_question_and_answer() -> (str, str):
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)
    operator = random.choice("+-*")
    question = f'{operand1} {operator} {operand2}'
    answer = get_arithmetic_expression_result(operand1, operand2, operator)
    return question, str(answer)
