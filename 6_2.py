from numba import jit

def parse_data_v2(data):
    """Combines numbers in each line into a single number, ignoring whitespaces."""
    lines = data.split('\n')
    times = int(''.join(lines[0].split()[1:]))
    distances = int(''.join(lines[1].split()[1:]))
    return times, distances


@jit(nopython=True)
def compute_counter(time, distance):
    counter = 0
    for k in range(time):
        if k * (time - k) > distance:
            counter += 1
    return counter

with open('input', 'r') as file:
    input_text = file.read()
    
time, distance = parse_data_v2(input_text)
counter = compute_counter(time, distance)

print("Margin of error:", counter)
