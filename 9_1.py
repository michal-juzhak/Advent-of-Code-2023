def get_sum_of_values_from_history(s):
    numbers = [int(n) for n in s.split()]
    all_deltas = [numbers]
    while all_deltas[-1].count(0) != len(all_deltas[-1]):
        new_deltas = [all_deltas[-1][i+1] - all_deltas[-1][i] for i in range(len(all_deltas[-1]) - 1)]
        all_deltas.append(new_deltas)
    return sum([lst[-1] for lst in all_deltas if lst])

def process_file(filename):
    sums = []
    with open(filename, 'r') as file:
        for line in file:
            line_sum = get_sum_of_values_from_history(line.strip())
            sums.append(line_sum)
    return sums

sums = process_file('input')
print(sum(sums))
