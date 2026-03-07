from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_parent_map(root):
    """
    Function name justification:
    build_parent_map -> clearly indicates we are building
    a mapping of child -> parent for traversal.

    Python convention: snake_case (PEP8).
    """

    parent_map = {}

    queue = deque([root])

    while queue:
        current_node = queue.popleft()

        if current_node.left:
            parent_map[current_node.left] = current_node
            queue.append(current_node.left)

        if current_node.right:
            parent_map[current_node.right] = current_node
            queue.append(current_node.right)

    return parent_map


def find_target_node(root, target_value):
    """
    Function name explanation:
    find_target_node -> explicit meaning: locate node
    whose value matches target.
    """

    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.value == target_value:
            return node

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return None


def burn_tree(root, target_value):
    """
    burn_tree -> main driver function controlling fire spread.
    """

    parent_map = build_parent_map(root)

    target_node = find_target_node(root, target_value)

    visited = set()

    queue = deque([target_node])
    visited.add(target_node)

    while queue:

        level_size = len(queue)
        current_level = []

        for _ in range(level_size):

            current_node = queue.popleft()
            current_level.append(current_node.value)

            # spread to left child
            if current_node.left and current_node.left not in visited:
                visited.add(current_node.left)
                queue.append(current_node.left)

            # spread to right child
            if current_node.right and current_node.right not in visited:
                visited.add(current_node.right)
                queue.append(current_node.right)

            # spread to parent
            if current_node in parent_map and parent_map[current_node] not in visited:
                visited.add(parent_map[current_node])
                queue.append(parent_map[current_node])

        print(current_level)
def build_tree_from_list(elements):
    """Helper to build a tree from a level-order list (LeetCode style)."""
    if not elements:
        return None
    
    root = Node(elements[0])
    queue = deque([root])
    i = 1
    while queue and i < len(elements):
        current = queue.popleft()
        
        # Left child
        if i < len(elements) and elements[i] is not None:
            current.left = Node(elements[i])
            queue.append(current.left)
        i += 1
        
        # Right child
        if i < len(elements) and elements[i] is not None:
            current.right = Node(elements[i])
            queue.append(current.right)
        i += 1
    return root

if __name__ == "__main__":
    # Input: root = [1, 5, 3, null, 4, 10, 6, 9, 2], start = 3
    # The tree structure:
    #          1
    #        /   \
    #       5     3 <--- Fire starts here
    #        \   / \
    #         4 10  6
    #        / \
    #       9   2
    
    tree_data = [1, 5, 3, None, 4, 10, 6, 9, 2]
    start_node_val = 3
    
    # 1. Build the tree
    root_node = build_tree_from_list(tree_data)
    
    print(f"Burning tree starting from node {start_node_val}:")
    
    # 2. Execute the burn_tree function
    # Note: Your function prints the levels directly.
    burn_tree(root_node, start_node_val)