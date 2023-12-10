from graphviz import Digraph

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def parse_input(data):
    nodes = {}
    for parent, children in data:
        if parent not in nodes:
            nodes[parent] = TreeNode(parent)
        if children[0] not in nodes:
            nodes[children[0]] = TreeNode(children[0])
        if children[1] not in nodes:
            nodes[children[1]] = TreeNode(children[1])

        nodes[parent].left = nodes[children[0]]
        nodes[parent].right = nodes[children[1]]

    return nodes

file_path = 'input'  

with open(file_path, 'r') as file:
    instructions = file.readline().strip('\n')
    next(file)
    next(file)

    input_data = []
    for line in file:
        parent, children_str = line.strip().split(' = ')
        children = tuple(children_str.strip('()').split(', '))
        input_data.append((parent, children))


nodes = parse_input(input_data)

root = nodes["AAA"]

'''def visualize_tree(root):
    dot = Digraph(comment='Tree')
    visited = set()

    def add_nodes_edges(node):
        if node and node.value not in visited:
            visited.add(node.value)
            dot.node(node.value)
            if node.left:
                dot.edge(node.value, node.left.value)
                add_nodes_edges(node.left)
            if node.right:
                dot.edge(node.value, node.right.value)
                add_nodes_edges(node.right)

    add_nodes_edges(root)
    dot.render('tree-output', view=True)'''

#visualize_tree(root)

def find_steps_to_target(root, target, instructions):
    current_node = root
    steps = 0
    i = 0  

    while current_node.value != target:
        if i >= len(instructions): 
            i = 0

        if instructions[i] == 'L' and current_node.left is not None:
            current_node = current_node.left
        elif instructions[i] == 'R' and current_node.right is not None:
            current_node = current_node.right
        else:
            return -1  

        steps += 1
        i += 1

    return steps

steps = find_steps_to_target(root, "ZZZ", instructions)
print(f"Number of steps from AAA to ZZZ: {steps}")
