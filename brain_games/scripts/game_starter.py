from brain_games.cli import game_play
from brain_games.cli import game_start_introduction
from brain_games.cli import game_end


def play(game_name: str, attempts=-1):
    user_name = game_start_introduction(game_name=game_name)
    result = game_play(game_name=game_name, attempts=attempts)
    game_end(user_name=user_name, win=result)


if __name__ == "__main__":
    pass
