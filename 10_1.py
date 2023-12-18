import networkx as nx

def parse_input(file_path):
    with open(file_path, 'r') as file:
        pipe_layout = []
        for line in file:
            row = list(line.strip())  
            pipe_layout.append(row)

    return pipe_layout

file_path = 'input_full'  
pipe_layout = parse_input(file_path)


def are_connected(piece1, piece2, direction):
    match_table = {
        '|': {'N': ['|', '7', 'F'], 'S': ['|', 'L', 'J'], 'E': [], 'W': []},
        '-': {'N': [], 'S': [], 'E': ['-', '7', 'J'], 'W': ['-', 'L', 'F']},
        'L': {'N': ['|', '7', 'F'], 'S': [], 'E': ['-', '7', 'J'], 'W': []},
        'J': {'N': ['|', '7', 'F'], 'S': [], 'E': [], 'W': ['-', 'L', 'F']},
        '7': {'N': [], 'S': ['|', 'L', 'J'], 'E': [], 'W': ['-', 'L', 'F']},
        'F': {'N': [], 'S': ['|', 'L', 'J'], 'E': ['-', '7', 'J'], 'W': []},
        'S': {'N': ['|', '7', 'F'], 'S': ['|', 'L', 'J'], 'E': ['-', '7', 'J'], 'W': ['-', 'L', 'F']}
    }

    return piece2 in match_table.get(piece1, {}).get(direction, [])

G = nx.Graph()

for i, row in enumerate(pipe_layout):
    for j, piece in enumerate(row):
        if piece != '.':
            node_name = (i, j)
            G.add_node(node_name, type=piece)

            if i > 0 and are_connected(piece, pipe_layout[i-1][j], 'N'):
                G.add_edge(node_name, (i-1, j))
            if i < len(pipe_layout) - 1 and are_connected(piece, pipe_layout[i+1][j], 'S'):
                G.add_edge(node_name, (i+1, j))
            if j > 0 and are_connected(piece, pipe_layout[i][j-1], 'W'):
                G.add_edge(node_name, (i, j-1))
            if j < len(row) - 1 and are_connected(piece, pipe_layout[i][j+1], 'E'):
                G.add_edge(node_name, (i, j+1))

start_node = [(i, j) for i, row in enumerate(pipe_layout) for j, piece in enumerate(row) if piece == 'S'][0]


def calculate_loop_details(G, start_node):
    path_lengths = nx.single_source_shortest_path_length(G, start_node)
    furthest_point, furthest_distance = max(path_lengths.items(), key=lambda x: x[1])

    return furthest_point, furthest_distance

furthest_point, furthest_distance = calculate_loop_details(G, start_node)
print(f"Furthest Point: {furthest_point}, Distance: {furthest_distance}")


