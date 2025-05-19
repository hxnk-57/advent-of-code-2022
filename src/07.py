from collections import defaultdict

FILE_PATH = "input/07.txt"

def get_sizes(lines):
    filepath = []
    sizes = defaultdict(int)

    for line in lines:
        if line == "$ ls":
            continue
        if line.startswith("$ cd"):
            if line == "$ cd /":
                filepath = ["/"]
            elif line == "$ cd ..":
                filepath.pop()
            else:
                dirname = line.split()[-1]
                filepath.append(dirname)
        else:
            filesize = line.split()[0]
            if filesize.isdigit():
                size = int(filesize)
                for i in range(len(filepath)):
                    dir_path = '/'.join(filepath[:i+1]).replace("//", "/")
                    sizes[dir_path] += size
    return sizes


def part_one(sizes) -> int:
    return sum(size for size in sizes.values() if size <= 100_000)


def part_two(sizes) -> int:
    space_to_free = sizes["/"] + 30_000_000 - 70_000_000
    return min(size for size in sizes.values() if size >= space_to_free)


if __name__ == "__main__":
    with open(FILE_PATH, 'r') as file:
        lines = [line.strip() for line in file]

    sizes = get_sizes(lines)
    print(f"Part One: {part_one(sizes)}")
    print(f"Part Two: {part_two(sizes)}")