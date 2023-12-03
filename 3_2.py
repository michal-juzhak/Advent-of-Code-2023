import numpy as np

def convert_to_2d_array(grid_str):
    lines = grid_str.strip().split('\n')
    return np.array([list(line) for line in lines])

def find_gears(array_2d):
    def has_two_digit_neighbours(slice_3x3):
        return sum(cell.isdigit() for row in slice_3x3 for cell in row) >= 2

    positions = []
    for i in range(1, array_2d.shape[0] - 1):
        for j in range(1, array_2d.shape[1] - 1):
            if array_2d[i, j] == '*':
                slice_3x3 = array_2d[i-1:i+2, j-1:j+2]
                if has_two_digit_neighbours(slice_3x3):
                    positions.append((i, j))

    return positions

def get_gear_ratios(array_2d):
    star_positions = find_gears(array_2d)

    def get_adjacent_digits(i, j):
        row = array_2d[i]

        left_index = j
        while left_index > 0 and row[left_index - 1].isdigit():
            left_index -= 1

        right_index = j
        while right_index < len(row) - 1 and row[right_index + 1].isdigit():
            right_index += 1

        return int(''.join(row[left_index:right_index + 1]))

    products = []
    for i, j in star_positions:
        adjacent_numbers = []
        for di in range(-1, 2):
            for dj in range(-1, 2):
                ni, nj = i + di, j + dj
                if 0 <= ni < array_2d.shape[0] and 0 <= nj < array_2d.shape[1]:
                    if array_2d[ni, nj].isdigit():
                        number = get_adjacent_digits(ni, nj)
                        if number not in adjacent_numbers:
                            adjacent_numbers.append(number)

        if len(adjacent_numbers) == 2:
            product = np.prod(adjacent_numbers)
            products.append(product)

    return np.array(products)

with open('input.txt', 'r') as file:
    grid_str = file.read()
    grid_array = convert_to_2d_array(grid_str)
    print(np.sum(get_gear_ratios(grid_array)))
