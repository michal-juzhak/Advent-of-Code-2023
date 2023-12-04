def get_card_id_and_matches(input_str):
    
    parts = input_str.split("|")
    game_id_str = parts[0].split(':')[0]
    game_id = int(game_id_str.replace('Card', '').strip())
    parts = input_str.split("|")   
    winning_numbers = set(int(num) for num in parts[0].split()[2:])  
    numbers_you_have = [int(num) for num in parts[1].split()]
    match_count = sum(1 for num in numbers_you_have if num in winning_numbers)    
    return match_count, game_id

with open('input.txt', 'r') as file:
    total_cards = sum(1 for _ in file)
    card_copies = {card_id: 1 for card_id in range(1, total_cards + 1)}

with open('input.txt', 'r') as file:
    for line in file:
        match_count, game_id = get_card_id_and_matches(line)
        current_copies = card_copies[game_id]

        for i in range(1, match_count + 1):
            next_card_id = (game_id + i - 1) % total_cards + 1
            card_copies[next_card_id] += current_copies

print(sum(card_copies.values()))
