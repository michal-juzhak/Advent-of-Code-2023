def analyze_game(line):

    game_id, color_data = line.split(':', 1)
    game_id = int(game_id.replace('Game', '').strip())
    segments = color_data.split(';')  
    max_red, max_blue, max_green = 0, 0, 0

    for segment in segments:
        pairs = segment.split(',')
        for pair in pairs:
            number, color = pair.strip().split()
            number = int(number)
            color = color.strip()
            if color == 'red':
                max_red = max(max_red, number)
            elif color == 'blue':
                max_blue = max(max_blue, number)
            elif color == 'green':
                max_green = max(max_green, number)

    return game_id, max_red, max_green, max_blue

total_sum = 0
with open('input.txt', 'r') as file:
    for line in file:
        game = analyze_game(line)
        power = game[1] * game[2] * game[3]
        total_sum += power
print (total_sum)
