from brain_games.cli import game_start_introduction
from brain_games.cli import game_play
from brain_games.cli import game_exit


def main():
    user_name = game_start_introduction(game_name='brain-even')
    result = game_play(game_name='brain-even')
    game_exit(user_name=user_name, win=result)


if __name__ == "__main__":
    pass

