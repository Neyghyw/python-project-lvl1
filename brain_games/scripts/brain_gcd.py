#!/usr/bin/env python
from brain_games.engine import start_game_template
from brain_games.games import gcd_game


def main():
    start_game_template(gcd_game)


if __name__ == "__main__":
    main()
