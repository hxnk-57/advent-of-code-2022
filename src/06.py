file_path = "input/06.txt"

with open(file_path, 'r') as file:    
    buffer = file.read()

def unique_window(window : str) -> bool:
        return len(window) == len(set(window))

def part_one() -> int:
    for i in range(0, len(buffer)):
        window = buffer[i:i+4]
        if unique_window(window):
            return i + 4


def part_two() -> int:
    for i in range(0, len(buffer)):
        window = buffer[i:i+14]
        if unique_window(window):
            return i + 14

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")