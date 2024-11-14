file_path = "input/03.txt"

with open(file_path, 'r') as file:    
    rucksacks = [line.strip() for line in file]

priority = {character: index + 1 for index, character in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}

def part_one() -> int:
    total = 0
    for rucksack in rucksacks:
        mid_point = len(rucksack) // 2
        compartment_one = set(rucksack[:mid_point])
        compartment_two = set(rucksack[mid_point:])
        duplicate_item = compartment_one.intersection(compartment_two).pop()
        total += priority[duplicate_item]
    return total


def part_two() -> int:
    total = 0

    for i in range(0, len(rucksacks), 3):
        group = [set(rucksacks[i]), set(rucksacks[i+1]), set(rucksacks[i+2])]
        group_badge = set.intersection(*group).pop()
        total += priority[group_badge]
    return total

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")