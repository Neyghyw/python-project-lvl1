import random


def gcd_get_question_and_answer() -> (str, str):
    value1 = random.randint(1, 100)
    value2 = random.randint(1, 100)
    start_position = min(value1, value2)
    nod_range = range(start_position, 0, -1)
    answer = 1
    for num in nod_range:
        if value1 % num == 0 and value2 % num == 0:
            answer = str(num)
            break
    question = f'{value1} {value2}'
    return question, answer
