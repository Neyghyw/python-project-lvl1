from brain_games.cli import game_play
from brain_games.cli import game_start_introduction
from brain_games.cli import game_end


def main():
    game = "brain_calc"
    user_name = game_start_introduction(game=game)
    result = game_play(game_name=game, attempts=1)
    game_end(user_name=user_name, win=result)


if __name__ == "__main__":
    main()
