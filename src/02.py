file_path = "input/02.txt"

games = []

with open(file_path, 'r') as file:
    games = [line.split() for line in file]


def part_one() -> int:
    scoring_rules = {
        "X": {"A": 4, "B": 1, "C": 7}, 
        "Y": {"A": 8, "B": 5, "C": 2},  
        "Z": {"A": 3, "B": 9, "C": 6} 
    }
    
    return sum(scoring_rules[my_move][opponent_move] for opponent_move, my_move  in games)


def part_two() -> int:
    scoring_rules = {
        "X": {"A": 3, "B": 1, "C": 2},  # Loss points
        "Y": {"A": 4, "B": 5, "C": 6},  # Draw points
        "Z": {"A": 8, "B": 9, "C": 7}   # Win points
    }

    return sum(scoring_rules[outcome][opponent] for opponent, outcome in games)

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")