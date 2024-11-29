file_path = "input/07.txt"

from Node import Node

with open(file_path, 'r') as file:    
    lines = [line.strip() for line in file]


def part_one() -> int:
    root = Node("/", is_directory=True)  # Root directory
    current_directory = root
    directory_stack = [current_directory]  # Stack to track parent directories

    for line in lines:
        if line.startswith("$ cd"):
            directory = line.split()[2]
            if directory == "..":
                # Move up one directory
                directory_stack.pop()
                current_directory = directory_stack[-1]
            else:
                # Move into a subdirectory
                new_directory = current_directory.find_node(directory)
                if not new_directory:
                    new_directory = Node(directory, is_directory=True)
                    current_directory.add_child(new_directory)
                current_directory = new_directory
                directory_stack.append(current_directory)

        elif line.startswith("$ ls"):
            # Ignored as we already parse individual lines
            continue

        elif line.startswith("dir"):
            directory_name = line.split()[1]
            new_directory = Node(directory_name, is_directory=True)
            current_directory.add_child(new_directory)

        else:
            # Line represents a file
            file_size, file_name = line.split()
            file_size = int(file_size)
            new_file = Node(file_name, is_directory=False)
            new_file.size = file_size
            current_directory.add_child(new_file)

    # Calculate folder sizes starting from the root
    root.calculate_folder_size()

    # Get all directory sizes
    directory_sizes = root.get_directory_sizes()

    print(directory_sizes)

    # Find the sum of all directories smaller than 100000
    result = sum(size for size in directory_sizes if size < 100000)

    print("Tree Structure with Sizes:")
    print(root)
    print(f"Sum of directories smaller than 100,000: {result}")
    return result

def part_two() -> int:
    return 

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")