import random


def get_question_and_answer(game):
    if game == "brain_calc":
        return calc_get_question_and_answer()
    elif game == "brain_even":
        return even_get_question_and_answer()
    elif game == "brain_gcd":
        return gcd_get_question_and_answer()
    elif game == "brain_progression":
        return progression_get_question_and_answer()


def calc_get_question_and_answer():
    value1 = random.randint(1, 100)
    value2 = random.randint(1, 100)
    operator = random.choice("+-*")
    question = f'{value1} {operator} {value2}'
    answer = str(eval(question))
    return question, answer


def even_get_question_and_answer():
    question = str(random.randint(1, 100))
    answer = (question % 2 == 0 and "yes") or "no"
    return question, answer


def gcd_get_question_and_answer():
    value1 = random.randint(1, 100)
    value2 = random.randint(1, 100)
    question = f'{value1} {value2}'
    answer = 1
    nod_range = range(min(value1, value2), 0, -1)
    for num in nod_range:
        if value1 % num == 0 and value2 % num == 0:
            answer = str(num)
            break
    return question, answer


def progression_get_question_and_answer():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    last_num = start + step * (10 - 1)
    question = ''
    for num in range(start, last_num, step):
        question += f'{num} '
    tup = question.rstrip().split(' ')
    answer = random.choice(tup)
    question = question.replace(answer, "..", 1)
    return question, answer


def print_rules(game):
    if game == "brain_calc":
        print('What is the result of the expression?')
    elif game == "brain_even":
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game == "brain_gcd":
        print('Find the greatest common divisor of given numbers.')
    elif game == "brain_progression":
        print('What number is missing in the progression?')


if __name__ == '__main__':
    pass
