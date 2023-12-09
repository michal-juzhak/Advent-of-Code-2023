from collections import Counter

def split_hands_and_bids(input_str):
    lines = input_str.strip().split("\n")
    list_of_tuples = []
    for line in lines:
        hand, bid = line.split()
        list_of_tuples.append((hand, bid))
    return list_of_tuples

def cards_to_hex(card_string):
    mapping = {'A': 'd', 'K': 'c', 'Q': 'b', 'T': 'a', 
               '9': '9', '8': '8', '7': '7', '6': '6', '5': '5', 
               '4': '4', '3': '3', '2': '2', 'J': '1'}

    hex_string = ''.join(mapping[card] for card in card_string)

    return hex_string

def is_n_of_a_kind(hand, n):
    if all(card == 'J' for card in hand):
        return n == 5  
    counts = Counter([card for card in hand if not (card == 'J')])
    jokers = hand.count('J')

    if list(counts.values()).count(2) == 2 and jokers == 1:  

        return False
    
    return any(count == (n - jokers) for count in counts.values())
    
def is_full_house(hand):
    counts = Counter(hand)
    jokers = counts.get('J', 0) 
    if 3 in counts.values() and 2 in counts.values():
        return True
    elif 3 in counts.values() and jokers == 1 and 'J' in hand:  
        return True
    elif list(counts.values()).count(2) == 2 and jokers == 1:
        return True
    return False


def is_two_pair(hand):
    counts = Counter(hand)
    return len([count for count in counts.values() if count == 2]) == 2

def process_hands(hands):
    list_2 = [(cards_to_hex(hand), bid) for hand, bid in hands]

    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []

    for hand, bid in hands:
        hex_hand = cards_to_hex(hand)  

        if is_n_of_a_kind(hand, 5):
            five_of_a_kind.append((hex_hand, bid))
            #print(hand, bid, '5')
        elif is_n_of_a_kind(hand, 4):
            four_of_a_kind.append((hex_hand, bid))
            #print(hand, bid, '4')
        elif is_full_house(hand):
            full_house.append((hex_hand, bid))
            #print(hand, bid, 'fh')
        elif is_n_of_a_kind(hand, 3):
            three_of_a_kind.append((hex_hand, bid))
            #print(hand, bid, '3')
        elif is_two_pair(hand):
            two_pair.append((hex_hand, bid))
            #print(hand, bid, '2 p')
        elif is_n_of_a_kind(hand, 2):
            one_pair.append((hex_hand, bid))
            #print(hand, bid, '2')
        else:
            high_card.append((hex_hand, bid))
            #print(hand, bid, 'h h')

    
    five_of_a_kind.sort(key=lambda x: int(x[0], 16), reverse=True)
    four_of_a_kind.sort(key=lambda x: int(x[0], 16), reverse=True)
    full_house.sort(key=lambda x: int(x[0], 16), reverse=True)
    three_of_a_kind.sort(key=lambda x: int(x[0], 16), reverse=True)
    two_pair.sort(key=lambda x: int(x[0], 16), reverse=True)
    one_pair.sort(key=lambda x: int(x[0], 16), reverse=True)
    high_card.sort(key=lambda x: int(x[0], 16), reverse=True)

    sorted_list = (five_of_a_kind + four_of_a_kind + full_house +
                   three_of_a_kind + two_pair + one_pair + high_card)

    return sorted_list

with open('input', 'r') as file:
    input_str = file.read()

 
game = split_hands_and_bids(input_str)
game_sorted = process_hands(game)
game_sorted.reverse()

sum = 0
counter = 1
for hand, bid in game_sorted:
    sum = sum + int(bid) * counter
    counter += 1

print (sum)
    
