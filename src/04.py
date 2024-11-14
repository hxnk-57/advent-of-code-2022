file_path = "input/04.txt"

with open(file_path, 'r') as file:    
    lines = [line.strip().split(",") for line in file]

def part_one() -> int:
    fully_contained_pairs = 0
    for line in lines:
        start1, end1 = map(int, line[0].split("-"))
        start2, end2 = map(int, line[1].split("-"))

        if (start1 >= start2 and end1 <= end2) or (start2 >= start1 and end2 <= end1):
            fully_contained_pairs += 1

    return fully_contained_pairs


def part_two() -> int:
    overlapping_pairs = 0
    for line in lines:
        start1, end1 = map(int, line[0].split("-"))
        start2, end2 = map(int, line[1].split("-"))

        if ((start2 >= start1 and start2 <= end1) or (start1 >= start2 and start1 <= end2)):
            overlapping_pairs += 1

    return overlapping_pairs

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")