file_path = "input/05.txt"

# [T]     [Q]             [S]        
# [R]     [M]             [L] [V] [G]
# [D] [V] [V]             [Q] [N] [C]
# [H] [T] [S] [C]         [V] [D] [Z]
# [Q] [J] [D] [M]     [Z] [C] [M] [F]
# [N] [B] [H] [N] [B] [W] [N] [J] [M]
# [P] [G] [R] [Z] [Z] [C] [Z] [G] [P]
# [B] [W] [N] [P] [D] [V] [G] [L] [T]
#  1   2   3   4   5   6   7   8   9 

stacks = {
    "1" : ['B', 'P', 'N', 'Q', 'H', 'D', 'R', 'T'],
    "2" : ['W', 'G', 'B', 'J', 'T', 'V'],
    "3" : ['N', 'R', 'H', 'D', 'S', 'V', 'M', 'Q'],
    "4" : ['P', 'Z', 'N', 'M', 'C'],
    "5" : ['D', 'Z', 'B'],
    "6" : ['V', 'C', 'W', 'Z'],
    "7" : ['G', 'Z', 'N', 'C', 'V', 'Q', 'L', 'S'],
    "8" : ['L', 'G', 'J', 'M', 'D', 'N', 'V'],
    "9" : ['T', 'P', 'M', 'F', 'Z', 'C', 'G'],
}

test_stacks = {
    "1" : ['Z', 'N'],
    "2" : ['M', 'C', 'D'],
    "3" : ['P'],
}

with open(file_path, 'r') as file:    
    instructions = [line.split() for line in file]

def part_one() -> str:
    solution = ""
    for instruction in instructions:
        count = int(instruction[1])
        source, destination = instruction[3], instruction[5]
        
        crates_to_move = stacks[source][-count:][::-1]
        stacks[source] = stacks[source][:-count]
        stacks[destination].extend(crates_to_move) 

    for stack in stacks.values():
        if stack:
            solution += stack[-1]
    return solution


def part_two() -> int:
    solution = ""
    for instruction in instructions:
        count = int(instruction[1])
        source, destination = instruction[3], instruction[5]
        
        crates_to_move = stacks[source][-count:]
        stacks[source] = stacks[source][:-count]
        stacks[destination].extend(crates_to_move) 
        
    for stack in stacks.values():
        if stack:
            solution += stack[-1]

    return solution

#print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")