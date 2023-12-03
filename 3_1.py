import numpy as np

def convert_to_2d_array(grid_str):
    lines = grid_str.strip().split('\n')
    return np.array([list(line) for line in lines])

def get_part_numbers(grid):
    numbers = []

    def has_special_neighbor(grid, i, j):
        neighborhood = grid[max(0, i - 1):i + 2, max(0, j - 1):j + 2]
        return np.any(np.logical_and(neighborhood != '.', ~np.char.isdigit(neighborhood)))

    def form_number(grid, i, j):
        num = ''
        start_j = j
        while j < grid.shape[1] and grid[i, j].isdigit():
            num += grid[i, j]
            j += 1
        for k in range(start_j, j):
            if has_special_neighbor(grid, i, k):
                return int(num)
        return None

    for i in range(grid.shape[0]):
        j = 0
        while j < grid.shape[1]:
            if grid[i, j].isdigit():
                num = form_number(grid, i, j)
                if num is not None:
                    numbers.append(num)              
                while j < grid.shape[1] and grid[i, j].isdigit():
                    j += 1
            else:
                j += 1
    return numbers

with open('input.txt', 'r') as file:
    grid_str = file.read()
    grid_array = convert_to_2d_array(grid_str)
    print(np.sum(get_part_numbers(grid_array)))
