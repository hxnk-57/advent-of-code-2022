from typing import List

file_path = "input/08.txt"

with open(file_path, 'r') as file:    
    lines = [line.strip() for line in file]
    forest = [[int(char) for char in line] for line in lines]


def is_visible(forest: List[List[int]], row: int, column: int) -> bool:
    tree = forest[row][column]
    # Check left
    if all(forest[row][i] < tree for i in range(column)):
        return True
    # Check right
    if all(forest[row][i] < tree for i in range(column + 1, len(forest[0]))):
        return True
    # Check top
    if all(forest[i][column] < tree for i in range(row)):
        return True
    # Check bottom
    if all(forest[i][column] < tree for i in range(row + 1, len(forest))):
        return True
    return False


def scenic_score(forest: List[List[int]], row: int, column: int) -> int:
    tree = forest[row][column]
    l = r = t = b = 0
    
    for i in range(column - 1, -1, -1):  # Start left of the tree and go to the start of the row
        if forest[row][i] >= tree:
            l += 1
            break
        l += 1

    for i in range(column + 1, len(forest[0])):  # Start right of the tree and go to the end of the row
        if forest[row][i] >= tree:
            r += 1
            break
        r += 1

    for i in range(row - 1, -1, -1):  # Start above the tree and go to the start of the column
        if forest[i][column] >= tree:
            t += 1
            break
        t += 1

    for i in range(row + 1, len(forest)):  # Start below the tree and go to the end of the column
        if forest[i][column] >= tree:
            b += 1
            break
        b += 1

    return l * r * t * b

def part_one() -> int:
    visible_trees = 0
    rows, columns = len(forest), len(forest[0])
    for row in range(rows):
        for column in range(columns):
            if row == 0 or column == 0 or row == rows - 1 or column == columns - 1:
                visible_trees += 1
            elif is_visible(forest, row, column):
                visible_trees += 1
    return visible_trees 

def part_two() -> int:
    highest_scenice_score = 0
    rows, columns = len(forest), len(forest[0])
    for row in range(rows):
        for column in range(columns):
            score = scenic_score(forest, row, column)
            if score >= highest_scenice_score:
                highest_scenice_score = score
    return highest_scenice_score 

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")