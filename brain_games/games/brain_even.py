import random


def even_get_question_and_answer() -> (str, str):
    question = random.randint(1, 100)
    answer = (question % 2 == 0 and "yes") or "no"
    return str(question), answer


if __name__ == "__main__":
    pass
