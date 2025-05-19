file_path = "input/09-test.txt"


with open(file_path, 'r') as file:    
    lines = [line.strip() for line in file]

head_path = [(0,0)]
tail_path = []

def part_one() -> int:
    head = (0,0)
    for line in lines:
        direction, units = line.split()
        for i in range(int(units)):
            if direction == "L":
                head = (head[0] - 1, head[1])
            if direction == "R":
                head = (head[0] + 1, head[1])
            if direction == "U":
                head = (head[0], head[1] + 1)
            if direction == "D":
                head = (head[0], head[1] - 1)
            head_path.append(head)      
    print(f"head path:{head_path}")

    tail_path = head_path.copy()

    for index, coordinate in enumerate(head_path[:-2]):
        if (head_path[index + 2][0] != coordinate[0] and head_path[index + 2][1] != coordinate[1]) or (head_path[index + 2][0] == coordinate[0] and head_path[index + 2][1] == coordinate[1]):
            print(f"corner detected at {head_path[index + 1]}")
            continue
        else:
            tail_path.remove(head_path[index + 1])
    
    print(tail_path)
    return len(head_path)- len(tail_path)


def part_two() -> int:
    return 


print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")