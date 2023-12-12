def get_reverse_deltas(s):

    numbers = [int(n) for n in s.split()]
    all_deltas = [numbers]
    while len(all_deltas[-1]) > 1:
        deltas = [all_deltas[-1][i+1] - all_deltas[-1][i] for i in range(len(all_deltas[-1]) - 1)]
        all_deltas.append(deltas)
    reverse_delta = 0
    for deltas in all_deltas[::-1]:
        reverse_delta = deltas[0] - reverse_delta
    return reverse_delta


def process_file(filename):
    sums = []
    with open(filename, 'r') as file:
        for line in file:
            line_sum = get_reverse_deltas(line.strip())
            sums.append(line_sum)
    return sums

sums = process_file('input')
print(sum(sums))
