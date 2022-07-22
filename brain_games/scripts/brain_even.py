import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string("May i have your name? ")
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    win_counter = 0
    while win_counter < 3:
        number = random.randint(1, 100)
        true_answer = (number % 2 == 0 and "yes") or "no"
        print(f'Question: {number}')
        user_answer = prompt.string("Your answer: ")
        if user_answer == true_answer:
            print('Correct!')
            win_counter += 1
        else:
            win_counter = 0
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{true_answer}'.")

    print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
