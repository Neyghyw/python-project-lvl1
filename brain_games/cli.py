import prompt
from brain_games.scripts.games_mechanics import get_question_and_answer
from brain_games.scripts.games_mechanics import print_rules


def game_start_introduction(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string("May i have your name? ")
    print(f'Hello, {user_name}!')
    print_rules(game)
    return user_name


def game_play(game_name, attempts=-1):
    wins = 0
    while wins < 3:
        if attempts == 0:
            return False
        question, true_answer = get_question_and_answer(game_name)
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if user_answer == true_answer:
            wins += 1
            print('Correct!')
        else:
            wins = 0
            attempts -= 1
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{true_answer}'.")
    return True


def game_end(user_name, win):
    if win:
        print(f"Congratulations, {user_name}!")
    else:
        print(f"Let's try again, {user_name}!")


if __name__ == '__main__':
    pass
