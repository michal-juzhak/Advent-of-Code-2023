from math import prod

def parse_data(data):
    
    lines = data.split('\n')
    times = [int(time) for time in lines[0].split()[1:]]
    distances = [int(distance) for distance in lines[1].split()[1:]]
    return times, distances


def number_of_ways(times, distances):
    
    counters = []
    for record_time, record_distance in zip(times, distances):
        counter = sum(1 for k in range(record_time) if k * (record_time - k) > record_distance)
        counters.append(counter)
    return counters


with open('input', 'r') as file:
    input_text = file.read()
    
times, distances = parse_data (input_text)
print("Margin of error:", prod(number_of_ways(times, distances)))
