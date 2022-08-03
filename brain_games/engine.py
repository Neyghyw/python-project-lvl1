import types
import prompt


def start_game_template(game_module: types.ModuleType):
    user_name = start_game_introduction(game_module=game_module)
    game_result = play_game(game_module=game_module)
    exit_game(user_name=user_name, is_win=game_result)


def start_game_introduction(game_module: types.ModuleType) -> str:
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_module.DESCRIPTION)
    return user_name


def play_game(game_module: types.ModuleType) -> bool:
    wins_count = 0
    while wins_count < 3:
        question, true_answer = game_module.get_game_data()
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
