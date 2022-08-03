import random
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
RANGE_START = 1
RANGE_END = 100


def get_game_data() -> (str, str):
    number1 = random.randint(RANGE_START, RANGE_END)
    number2 = random.randint(RANGE_START, RANGE_END)
    answer = str(math.gcd(number1, number2))
    question = f'{number1} {number2}'
    game_data = question, answer
    return game_data
