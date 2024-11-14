file_path = r"2022\input\01.txt"

lines = []
elves = []

with open(file_path, 'r') as file:
     lines = [line.strip() for line in file]   

def part_one() -> int:
    current_elf = 0
    for line in lines:
        if line:
            current_elf += int(line)
        else:
            elves.append(int(current_elf))
            current_elf = 0

    return max(elves)  


def part_two() -> int:
    elves.sort(reverse=True)
    return sum(elves[:3])

print(part_one())
print(part_two())