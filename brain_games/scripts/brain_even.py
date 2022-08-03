#!/usr/bin/env python
from brain_games import engine
from brain_games.games import even


def main():
    engine.start_game_template(even)


if __name__ == '__main__':
    main()
