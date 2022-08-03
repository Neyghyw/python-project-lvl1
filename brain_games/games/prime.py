import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no"'
RANGE_START = 2
RANGE_END = 250


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def get_game_data() -> (str, str):
    question = random.randint(RANGE_START, RANGE_END)
    answer = is_prime(question) and 'yes' or 'no'
    game_data = str(question), answer
    return game_data
