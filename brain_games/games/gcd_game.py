import random
import math

RULES = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer() -> (str, str):
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    answer = str(math.gcd(number1, number2))
    question = f'{number1} {number2}'
    return question, answer
