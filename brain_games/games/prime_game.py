import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def is_prime(number: int) -> bool:
    for divisor in range(2, number):
        if number % divisor == 0 and number > 2:
            return False
    return True


def get_question_and_answer() -> (str, str):
    question = random.randint(2, 250)
    answer = is_prime(question) and 'yes' or 'no'
    return str(question), answer
