#!/usr/bin/env python
from brain_games.games import game_engine, progression_game


def main():
    game_engine.start_game_template(progression_game)


if __name__ == "__main__":
    main()
