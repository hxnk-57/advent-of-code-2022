class Node:
    def __init__(self, name, is_directory=True):
        self.name = name 
        self.is_directory = is_directory
        self.children = []
        self.size = 0

    def add_child(self, child_node):
        self.children.append(child_node)

    def find_node(self, name):
        """Recursively search for a node with the given value."""
        # Check the current node first
        if self.name == name:
            return self
        # Search in children recursively
        for child in self.children:
            found = child.find_node(name)
            if found:
                return found
        return None
    
    def calculate_folder_size(self):
        """Recursively calculate the size of the folder."""
        if not self.is_directory:
            return self.size  # Return the file size
        total_size = 0
        for child in self.children:
            total_size += child.calculate_folder_size()
        self.size = total_size  # Update the folder's size
        return self.size
    
    def get_directory_sizes(self):
        """Collect sizes of all directories in the tree."""
        sizes = []
        if self.is_directory:
            sizes.append(self.size)  # Add the size of the current directory
        for child in self.children:
            sizes.extend(child.get_directory_sizes())  # Recurse into children
        return sizes

    def __repr__(self, level=0):
        indent = "\t" * level
        if self.is_directory:
            ret = f"{indent}[DIR] {self.name} (Size: {self.size})\n"
        else:
            ret = f"{indent}[FILE] {self.name} (Size: {self.size})\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret