import random


def calc_get_question_and_answer() -> (str, str):
    value1 = random.randint(1, 100)
    value2 = random.randint(1, 100)
    operator = random.choice("+-*")
    question = f'{value1} {operator} {value2}'
    answer = str(eval(question))
    return question, answer


if __name__ == "__main__":
    pass
