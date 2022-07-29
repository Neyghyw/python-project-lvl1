#!/usr/bin/env python
from brain_games.games import even_game
from brain_games import game_engine


def main():
    game_engine.start_game_template(even_game)


if __name__ == "__main__":
    main()
