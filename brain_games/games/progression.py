import random

DESCRIPTION = 'What number is missing in the progression?'
RANGE_START = 1
RANGE_END = 10
PROGRESSION_LEN = 10


def get_game_data() -> (str, str):
    progression_step = random.randint(RANGE_START, RANGE_END)
    first_num = random.randint(RANGE_START, RANGE_END)
    last_num = first_num + progression_step * (PROGRESSION_LEN - 1)
    question = ''
    for num in range(first_num, last_num, progression_step):
        question += f'{num} '
    progression_tuple = question.rstrip().split(' ')
    answer = random.choice(progression_tuple)
    question = question.replace(answer, '..', 1)
    game_data = question, answer
    return game_data
