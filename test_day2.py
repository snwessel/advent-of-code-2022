import day2


def test_get_round_outcome_points():
    assert day2.get_round_outcome_points(you_enum=day2.Play.PAPER, opponent_enum=day2.Play.ROCK) == 6
    assert day2.get_round_outcome_points(you_enum=day2.Play.ROCK, opponent_enum=day2.Play.PAPER) == 0
    assert day2.get_round_outcome_points(you_enum=day2.Play.SCISSORS, opponent_enum=day2.Play.SCISSORS) == 3

def test_score_round():
    assert day2.score_round(you="Y", opponent="A") == 8
    assert day2.score_round(you="X", opponent="B") == 1
    assert day2.score_round(you="Z", opponent="C") == 6

def test_parse_outcomes():
    assert day2.total_outcomes('./test_inputs/day2.txt') == 15

# PART 2

def test_calculate_your_move():
    assert day2.calculate_your_move(opponent_enum=day2.Play.ROCK, outcome_code="Y") == day2.Play.ROCK

def test_parse_outcomes_part2():
    assert day2.total_outcomes_part2('./test_inputs/day2.txt') == 12