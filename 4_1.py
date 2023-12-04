def calculate_card_total_worth(input_str):

    parts = input_str.split("|")   
    winning_numbers = set(int(num) for num in parts[0].split()[2:])  
    numbers_you_have = [int(num) for num in parts[1].split()]
    match_count = sum(1 for num in numbers_you_have if num in winning_numbers)    
    return 2 ** (match_count - 1) if match_count > 0 else 0

i = 0
with open('input.txt', 'r') as file:
    for line in file:
        value = calculate_card_total_worth(line)
        i += value
    print(f"Sum = {i}")
