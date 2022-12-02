from enum import Enum

# PART 1

class Play(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

code_to_play_enum = {
    "A": Play.ROCK,
    "B": Play.PAPER,
    "C": Play.SCISSORS,
    "X": Play.ROCK,
    "Y": Play.PAPER,
    "Z": Play.SCISSORS,
}


def total_outcomes(input_filename):
    total_score = 0
    with open(input_filename) as f:
        lines = f.readlines()
        for line in lines:
            opponent, you = line.strip().split(" ")
            total_score += score_round(you, opponent)
    return total_score


def score_round(you, opponent):
    # decode the plays
    you_enum = code_to_play_enum[you]
    opponent_enum = code_to_play_enum[opponent]
    return get_round_points(you_enum, opponent_enum)

def get_round_points(you_enum, opponent_enum):
    play_type_points = you_enum.value
    outcome_points = get_round_outcome_points(you_enum, opponent_enum)
    # print(you_enum.name, "+", opponent_enum.name, "=", play_type_points, "+", outcome_points)
    return play_type_points + outcome_points


def get_round_outcome_points(you_enum, opponent_enum):
    # use modulos to figure out who won
    mod_output = (you_enum.value - opponent_enum.value) % 3
    # Example: rock - paper = (1 - 2) % 3 = -1 % 3 = 2 -> Lose! 
    # Example: scissors - rock = (3 - 1) % 3 = 2 % 3 = 2 -> Lose!
    # Example: paper - rock = (2 - 1) % 3 = 1 % 3 = 1 -> Win!
    if mod_output == 2: # you lose
        return 0
    if mod_output == 0: # you tie
        return 3
    if mod_output == 1: # you win
        return 6


print(total_outcomes('./inputs/day2.txt'))


# PART 2
code_to_move_direction = {
    "X": -1, # to lose, play the move with one less in value
    "Y": 0, # to tie, play the move with the same enum value
    "Z": 1, # to win, play the move with one more in value
}

def total_outcomes_part2(input_filename):
    total_score = 0
    with open(input_filename) as f:
        lines = f.readlines()
        for line in lines:
            opponent, outcome_code = line.strip().split(" ")
            total_score += score_round_part2(opponent, outcome_code)
    return total_score

def score_round_part2(opponent, outcome_code):
    # decode the plays
    opponent_enum = code_to_play_enum[opponent]
    you_enum = calculate_your_move(opponent_enum, outcome_code)
    return get_round_points(you_enum, opponent_enum)

def calculate_your_move(opponent_enum, outcome_code):
    move_direction = code_to_move_direction[outcome_code]
    return Play((opponent_enum.value + move_direction - 1) % 3 + 1)

print(total_outcomes_part2('./inputs/day2.txt'))