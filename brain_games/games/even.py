import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
RANGE_START = 1
RANGE_END = 100


def get_game_data() -> (str, str):
    question = random.randint(RANGE_START, RANGE_END)
    answer = (question % 2 == 0 and 'yes') or 'no'
    game_data = str(question), answer
    return game_data
