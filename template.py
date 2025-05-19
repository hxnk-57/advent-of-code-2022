file_path = "input/0.txt"

with open(file_path, 'r') as file:    
    lines = [line.strip() for line in file]

def part_one() -> int:
    print(lines)
    for line in lines:
        print(line)
    return 

def part_two() -> int:
    return 

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")