#!/usr/bin/env python
import prompt

from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string(prompt='May i have your name? ')
    welcome_user(user_name)


if __name__ == '__main__':
    main()
