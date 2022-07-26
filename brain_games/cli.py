import prompt
from brain_games.utils.game_data import rules
from brain_games.utils.game_data import question_and_answer


def game_template_start(game_name: str):
    user_name = game_start_introduction(game_name=game_name)
    result = game_play(game_name=game_name)
    game_exit(user_name=user_name, win=result)


def game_start_introduction(game_name: str) -> str:
    print('Welcome to the Brain Games!')
    user_name = prompt.string("May I have your name? ")
    print(f'Hello, {user_name}!')
    print(rules.get(game_name))
    return user_name


def game_exit(user_name: str, win: bool):
    if win:
        print(f"Congratulations, {user_name}!")
    else:
        print(f"Let's try again, {user_name}!")


def game_play(game_name: str) -> bool:
    wins = 0
    while wins < 3:
        question, true_answer = question_and_answer[game_name]()
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if user_answer == true_answer:
            wins += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{true_answer}'.")
            return False
    return True


if __name__ == '__main__':
    pass
