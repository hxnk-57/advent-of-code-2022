file_path = r"input\02.txt"

def part_one() -> int:
    total = 0

    with open(file_path, 'r') as file:    
        games = [line.strip().replace(" ", "") for line in file]
    
    scores = {
        'BX': 1,
        'CY': 2,
        'AZ': 3,
        'AX': 4,
        'BY': 5,
        'CZ': 6,
        'CX': 7,
        'AY': 8,
        'BZ': 9
    }

    for round in games:
        total += scores[round]
    return total

# A rock
# B paper
# C Scissors
# X Lose 
# Y Draw
# Z Win

def part_two() -> int:
    total = 0

    with open(file_path, 'r') as file:    
        games = [line.split() for line in file]

    for round in games:
        opponent = round[0]
        outcome = round[1]

        if outcome == "X": # You lost
            if opponent == "A": # Opponent played rock
                total += 3 # You played scissors.
            elif opponent == "B": # Opponent played paper
                total += 1 # You played rock
            else: # opponent played scissors
                total += 2 # You played paper.

        elif outcome == "Y": # The round was a draw
            # Award points for the outcome.
            total += 3
            if opponent == "A": # Opponent played rock
                total += 1 # You played rock.
            elif opponent == "B": # Opponent played paper
                total += 2 # You played paper
            else: # opponent played scissors
                total += 3 # You played scissors.
        
        else: # You won the round
            # Award points for the outcome.
            total += 6
            if opponent == "A": # Opponent played rock
                total += 2 # You played paper.
            elif opponent == "B": # Opponent played paper
                total += 3 # You played scissor
            else: # opponent played scissors
                total += 1 # You played rock.
        

    return total

print(f"Part One {part_one()}")
print(f"Part Two {part_two()}")