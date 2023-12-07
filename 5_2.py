def parse_almanac(input_text):
    
    segments = input_text.strip().split('\n\n')
    almanac = {}

    for segment in segments:
        lines = segment.split('\n')
        section_name, values = lines[0].split(':', 1)

        if section_name.strip() == 'seeds':
            almanac[section_name.strip()] = list(map(int, values.strip().split()))
        else:
            map_name = section_name.replace(' map', '').replace('-', '_').strip()
            map_values = [list(map(int, line.replace(',', ' ').split())) for line in lines[1:]]
            almanac[map_name] = map_values

    return almanac

def reverse_transform_location(location, maps):
    for map_name in reversed(['seed_to_soil', 'soil_to_fertilizer', 'fertilizer_to_water', 
                              'water_to_light', 'light_to_temperature', 
                              'temperature_to_humidity', 'humidity_to_location']):
        map_data = maps[map_name]
        for map_entry in map_data:
            destination_range_start, source_range_start, range_value = map_entry
            if destination_range_start <= location < (destination_range_start + range_value):
                location = location - (destination_range_start - source_range_start)
                break
            
    return location

def update_almanac_reduced(almanac):
    updated_almanac = almanac.copy()
    seeds = updated_almanac['seeds']

    new_seeds = []
    for i in range(0, len(seeds), 2):
        seed = seeds[i]
        if i + 1 < len(seeds):
            range_value = seeds[i + 1]
            new_seeds.append((seed, seed + range_value))
        else:
            new_seeds.append((seed, seed + 1))  
    updated_almanac['seeds'] = new_seeds

    return updated_almanac

def find_smallest_valid_location(almanac):
    start_points = [entry[0] for entry in almanac['humidity_to_location']]
    start_points.sort()

    for start_point in start_points:
        transformed_seed = reverse_transform_location(start_point, almanac)
        for seed_range in almanac['seeds']:
            if seed_range[0] <= transformed_seed < seed_range[1]:
                return start_point

    return None  

with open('input', 'r') as file:
    input_text = file.read()

almanac = parse_almanac(input_text)
updated_almanac = update_almanac_reduced(almanac)
smallest_location = find_smallest_valid_location(updated_almanac)
print(smallest_location)
