import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def get_prime_question_and_answer() -> (str, str):
    question = random.randint(1, 250)
    answer = 'yes'
    for divisor in range(2, question):
        if question % divisor == 0:
            answer = 'no'
            break
    return str(question), answer
