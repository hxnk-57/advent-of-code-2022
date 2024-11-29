file_path = "input/10.txt"

with open(file_path, 'r') as file:    
    lines = [line.strip() for line in file]

def check_signal_strength(cycle):
    return (cycle == 20) or (cycle % 40 == 20 and 0 < cycle <= 220)

def part_one() -> int:
    current_cycle = 0
    x = 1
    signal_strength = 0

    for line in lines:
        current_cycle += 1
        if check_signal_strength(current_cycle):
            signal_strength += current_cycle * x
        if line.startswith("addx"):
            current_cycle += 1
            if check_signal_strength(current_cycle):
                signal_strength += current_cycle * x
            x += int(line.split()[1])

    return signal_strength

def part_two() -> int:
    return 

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")