from brain_games.utils import even_utils
from brain_games.utils import calc_utils
from brain_games.utils import prime_utils
from brain_games.utils import progression_utils
from brain_games.utils import gcd_utils


question_and_answer = {
    'brain-calc': calc_utils.calc_get_question_and_answer,
    'brain-even': even_utils.even_get_question_and_answer,
    'brain-gcd': gcd_utils.gcd_get_question_and_answer,
    'brain-progression': progression_utils.progression_get_question_and_answer,
    'brain-prime': prime_utils.prime_get_question_and_answer
}


rules = {
    'brain-calc': calc_utils.RULES,
    'brain-even': even_utils.RULES,
    'brain-gcd': gcd_utils.RULES,
    'brain-progression': progression_utils.RULES,
    'brain-prime': prime_utils.RULES
}
