import re

def find_first_last_digit(line):
    digits = re.findall(r'\d', line)
    digits = [int(num) for num in digits]

    if not digits:
        return None, None 

    return (digits[0]*10 + digits[-1])

i = 0
with open('input.txt', 'r') as file:
    for line in file:
        value = find_first_last_digit(line)
        i += value
    print(f"Sum = {i}")
