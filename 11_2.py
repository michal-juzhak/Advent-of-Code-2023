import numpy as np
from itertools import combinations

with open('input', 'r') as file:
    lines = file.readlines()

grid = np.array([list(line.strip()) for line in lines])

empty_rows = [i for i, row in enumerate(grid) if np.all(row == '.')]
empty_cols = [j for j, col in enumerate(grid.T) if np.all(col == '.')]

counter = 1000000

positions = []  
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == '#':
            adjusted_i = i + sum(1 for er in empty_rows if er < i) * (counter - 1)
            adjusted_j = j + sum(1 for ec in empty_cols if ec < j) * (counter - 1)
            positions.append((adjusted_i, adjusted_j))

total_distance = 0
for pos1, pos2 in combinations(positions, 2):
    distance = abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])
    total_distance += distance

print(f"Total sum of distances: {total_distance}")
