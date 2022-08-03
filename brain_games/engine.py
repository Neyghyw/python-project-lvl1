import types
import prompt


ROUNDS_COUNT = 3


def play_game(game_module: types.ModuleType):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_module.DESCRIPTION)

    wins_count = 0
    while wins_count < ROUNDS_COUNT:
        question, true_answer = game_module.get_game_data()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if not user_answer == true_answer:
            print(f'\'{user_answer}\' is wrong answer ;(.'
                  f' Correct answer was \'{true_answer}\'.')
            break
        wins_count += 1
        print('Correct!')

    if wins_count == ROUNDS_COUNT:
        print(f'Congratulations, {user_name}!')
    else:
        print(f'Let\'s try again, {user_name}!')


if __name__ == '__main__':
    pass
