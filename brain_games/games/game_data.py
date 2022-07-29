from brain_games.games import even_game
from brain_games.games import calc_game
from brain_games.games import prime_game
from brain_games.games import progression_game
from brain_games.games import gcd_game


question_and_answer = {
    'brain-calc': calc_game.get_calc_question_and_answer,
    'brain-even': even_game.get_even_question_and_answer,
    'brain-gcd': gcd_game.get_gcd_question_and_answer,
    'brain-progression': progression_game.get_progression_question_and_answer,
    'brain-prime': prime_game.get_prime_question_and_answer
}


rules = {
    'brain-calc': calc_game.RULES,
    'brain-even': even_game.RULES,
    'brain-gcd': gcd_game.RULES,
    'brain-progression': progression_game.RULES,
    'brain-prime': prime_game.RULES
}
