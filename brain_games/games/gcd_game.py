import random


RULES = 'Find the greatest common divisor of given numbers.'


def get_gcd_question_and_answer() -> (str, str):
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    start_position = min(number1, number2)
    gcd_range = range(start_position, 0, -1)
    answer = 1
    for divisor in gcd_range:
        if number1 % divisor == 0 and number2 % divisor == 0:
            answer = str(divisor)
            break
    question = f'{number1} {number2}'
    return question, answer
