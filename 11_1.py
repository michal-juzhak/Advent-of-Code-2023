import numpy as np
from itertools import combinations

with open('input', 'r') as file:
    lines = file.readlines()

grid = [list(line.strip()) for line in lines]

new_grid = []
for row in grid:
    new_grid.append(row)
    if all(cell == '.' for cell in row):
        new_grid.append(['.' for _ in row])

grid_array = np.array(new_grid)

transposed_array = grid_array.T

new_transposed_array = []
for col in transposed_array:
    new_transposed_array.append(col)
    if all(cell == '.' for cell in col):
        new_transposed_array.append(['.' for _ in col])

expanded_array = np.array(new_transposed_array).T

hash_count = 1
positions = {}
for i, row in enumerate(expanded_array):
    for j, cell in enumerate(row):
        if cell == '#':
            expanded_array[i, j] = str(hash_count)
            positions[hash_count] = (i, j)
            hash_count += 1

total_distance = 0
for (num1, pos1), (num2, pos2) in combinations(positions.items(), 2):
    distance = abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])
    total_distance += distance

print(f"Total sum of distances: {total_distance}")
