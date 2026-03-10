# LC 2385. Amount of Time for Binary Tree to Be Infected
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def burn_subtree(node, time, result):
    """
    DFS helper to burn nodes downward.
    """
    if node is None:
        return
    if len(result) <= time:
        result.append([])
    result[time].append(node.value)
    burn_subtree(node.left, time + 1, result)
    burn_subtree(node.right, time + 1, result)

def dfs(node, target, result):
    """
    DFS to locate target and propagate burn upwards.
    """
    if node is None:
        return -1
    if node.value == target:
        burn_subtree(node, 0, result)
        return 1
    left_distance = dfs(node.left, target, result)
    if left_distance != -1:
        if len(result) <= left_distance:
            result.append([])
        result[left_distance].append(node.value)
        burn_subtree(node.right, left_distance + 1, result)
        return left_distance + 1
    right_distance = dfs(node.right, target, result)
    if right_distance != -1:
        if len(result) <= right_distance:
            result.append([])
        result[right_distance].append(node.value)
        burn_subtree(node.left, right_distance + 1, result)
        return right_distance + 1
    return -1

def burn_tree(root, target):
    result = []
    dfs(root, target, result)
    for level in result:
        print(level)
def build_tree(elements):
    """Helper to build a tree from a level-order list."""
    if not elements:
        return None
    nodes = [Node(val) if val is not None else None for val in elements]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root
if __name__ == "__main__":
    # Input representation: [1, 5, 3, null, 4, 10, 6, 9, 2]
    # Structure:
    #        1
    #       / \
    #      5   3
    #       \ / \
    #       4 10 6
    #      / \
    #     9   2
    
    tree_input = [1, 5, 3, None, 4, 10, 6, 9, 2]
    target_val = 3
    
    root_node = build_tree(tree_input)
    
    print(f"Burning tree starting from node: {target_val}")
    print("Nodes burned at each second:")
    
    # Executing your logic
    result_list = []
    dfs(root_node, target_val, result_list)
    
    for i, level in enumerate(result_list):
        print(f"Time {i}: {level}")
    
    print(f"\nTotal time to burn: {len(result_list) - 1} seconds")