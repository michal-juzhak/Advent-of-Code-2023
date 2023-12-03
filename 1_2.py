def get_calibration_value(line):
    number_words = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    reversed_number_words = {word[::-1]: num for word, num in number_words.items()}

    def find_first_number(s, words_dict):
        for i in range(len(s)):
            for word in words_dict:
                if s[i:].startswith(word):
                    return words_dict[word]
            if s[i].isdigit():
                return int(s[i])
        return None

    first_number = find_first_number(line.lower(), number_words)
    last_number = find_first_number(line[::-1].lower(), reversed_number_words)
    calibiration_value = first_number * 10 + last_number

    return calibiration_value

total_sum = 0
with open('input.txt', 'r') as file:
    for line in file:
        calibration_value = get_calibration_value(line.strip()) 
        
        if calibration_value is not None:
            total_sum += calibration_value

print(f"Sum = {total_sum}")
