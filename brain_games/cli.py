import prompt
from brain_games.scripts.games_mechanics import get_question_and_answer
from brain_games.scripts.games_mechanics import print_rules


def game_template(game, chances=None):
    print('Welcome to the Brain Games!')
    user_name = prompt.string("May i have your name? ")
    print(f'Hello, {user_name}!')
    
    print_rules(game)

    wins, loses = 0, 0
    while wins < 3:
        if loses == chances:
            print(f"Let's try again, {user_name}!")
            break
        question, true_answer = get_question_and_answer(game)
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if user_answer == true_answer:
            wins += 1
            print('Correct!')
        else:
            wins = 0
            loses += 1
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{true_answer}'.")

    if wins == 3:
        print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    pass
