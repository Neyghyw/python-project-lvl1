import random


def prime_get_question_and_answer() -> (str, str):
    question = random.randint(1, 250)
    answer = 'yes'
    for i in range(2, question):
        if question % i == 0:
            answer = 'no'
            break
    return str(question), answer
