from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def process_input(input_text):
    lines = input_text.strip().split('\n')
    instructions = lines[0].strip()
    map_array = []
    for line in lines[1:]:
        if not line.strip():
            continue

        key, values = line.split('=')
        value1, value2 = values.strip()[1:-1].split(', ')
        map_array.append([key.strip(), value1, value2])

    return instructions, map_array

def find_steps_for_path(start_element, map_array, instructions, max_steps):
    index_map = {row[0]: i for i, row in enumerate(map_array)}
    steps = 0
    instruction_index = 0
    current_element = start_element

    while steps < max_steps:
        if current_element.endswith('Z'):
            return steps
        next_element_index = index_map.get(current_element)
        if next_element_index is None:
            break
        next_element = map_array[next_element_index][1 if instructions[instruction_index] == 'L' else 2]
        instruction_index = (instruction_index + 1) % len(instructions)
        steps += 1
        current_element = next_element

    return -1  

def find_simultaneous_steps_lcm(map_array, instructions, max_steps=1000000000000):
    starting_elements = [row[0] for row in map_array if row[0].endswith('A')]
    path_steps = []

    for element in starting_elements:
        steps = find_steps_for_path(element, map_array, instructions, max_steps)
        if steps == -1:
            return -1  
        path_steps.append(steps)

    return reduce(lcm, path_steps)

file_path = 'input'
with open(file_path, 'r') as file:
    input_text = file.read()

instructions, map_array = process_input(input_text)
a = find_simultaneous_steps_lcm(map_array, instructions)
print(a)
