from brain_games.games import even_utils
from brain_games.games import calc_utils
from brain_games.games import prime_utils
from brain_games.games import progression_utils
from brain_games.games import gcd_utils


question_and_answer = {
    'brain-calc': calc_utils.get_calc_question_and_answer,
    'brain-even': even_utils.get_even_question_and_answer,
    'brain-gcd': gcd_utils.get_gcd_question_and_answer,
    'brain-progression': progression_utils.get_progression_question_and_answer,
    'brain-prime': prime_utils.get_prime_question_and_answer
}


rules = {
    'brain-calc': calc_utils.RULES,
    'brain-even': even_utils.RULES,
    'brain-gcd': gcd_utils.RULES,
    'brain-progression': progression_utils.RULES,
    'brain-prime': prime_utils.RULES
}
