#!/usr/bin/env python
from brain_games import game_engine, games


def main():
    game_engine.start_game_template(games.even_game)


if __name__ == "__main__":
    main()
