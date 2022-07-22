import random


def get_question_and_answer(game):
    if game == "brain_calc":
        return calc_get_question_and_answer()
    elif game == "brain_even":
        return even_get_question_and_answer()


def calc_get_question_and_answer():
    value1 = random.randint(1, 100)
    value2 = random.randint(1, 100)
    operator = random.choice("+-*")
    question = f'{value1} {operator} {value2}'
    answer = str(eval(question))
    return question, answer


def even_get_question_and_answer():
    question = random.randint(1, 100)
    answer = (question % 2 == 0 and "yes") or "no"
    return question, answer


def print_rules(game):
    if game == "brain_calc":
        print('What is the result of the expression?')
    elif game == "brain_even":
        print('Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == '__main__':
    pass
