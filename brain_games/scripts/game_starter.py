from brain_games.cli import game_start_introduction
from brain_games.cli import game_play
from brain_games.cli import game_exit
import sys


def main():
    script_name = sys.argv[0]
    user_name = game_start_introduction(game_name=script_name)
    result = game_play(game_name=script_name)
    game_exit(user_name=user_name, win=result)


if __name__ == "__main__":
    pass
