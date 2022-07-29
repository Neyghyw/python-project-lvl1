import prompt
from brain_games.games.game_data import rules
from brain_games.games.game_data import question_and_answer


def start_game_template(game_name: str):
    user_name = start_game_introduction(game_name=game_name)
    game_result = play_game(game_name=game_name)
    exit_game(user_name=user_name, is_win=game_result)


def start_game_introduction(game_name: str) -> str:
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(rules.get(game_name))
    return user_name


def play_game(game_name: str) -> bool:
    wins_count = 0
    while wins_count < 3:
        question, true_answer = question_and_answer[game_name]()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if not user_answer == true_answer:
            print(f'\'{user_answer}\' is wrong answer ;(.'
                  f' Correct answer was \'{true_answer}\'.')
            return False
        wins_count += 1
        print('Correct!')
    return True


def exit_game(user_name: str, is_win: bool):
    if is_win:
        print(f'Congratulations, {user_name}!')
    else:
        print(f'Let\'s try again, {user_name}!')


if __name__ == '__main__':
    pass
