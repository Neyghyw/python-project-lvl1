import random


def get_question_and_answer(game_name: str) -> (str, str):
    question_and_answer = {
        'brain_calc': calc_get_question_and_answer(),
        'brain_even': even_get_question_and_answer(),
        'brain_gcd': gcd_get_question_and_answer(),
        'brain_progression': progression_get_question_and_answer(),
        'brain_prime': prime_get_question_and_answer()
    }
    return question_and_answer.get(game_name)


def even_get_question_and_answer() -> (str, str):
    question = random.randint(1, 100)
    answer = (question % 2 == 0 and "yes") or "no"
    return str(question), answer


def prime_get_question_and_answer() -> (str, str):
    question = random.randint(1, 250)
    answer = 'yes'
    for i in range(2, question):
        if question % i == 0:
            answer = 'no'
            break
    return str(question), answer


def calc_get_question_and_answer() -> (str, str):
    value1 = random.randint(1, 100)
    value2 = random.randint(1, 100)
    operator = random.choice("+-*")
    question = f'{value1} {operator} {value2}'
    answer = str(eval(question))
    return question, answer


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


def progression_get_question_and_answer() -> (str, str):
    progression_step = random.randint(1, 10)
    first_num = random.randint(1, 50)
    last_num = first_num + progression_step * (10 - 1)
    question = ''
    for num in range(first_num, last_num, progression_step):
        question += f'{num} '
    progression_tuple = question.rstrip().split(' ')
    answer = random.choice(progression_tuple)
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
    elif game == "brain_prime":
        print('Answer "yes" if given number is prime. Otherwise answer "no"')


if __name__ == '__main__':
    pass
