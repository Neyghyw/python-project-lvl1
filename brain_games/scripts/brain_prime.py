#!/usr/bin/env python
from brain_games.games import prime_game
from brain_games import game_engine


def main():
    game_engine.start_game_template(prime_game)


if __name__ == "__main__":
    main()
