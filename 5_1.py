def parse_almanac(input_text):
    segments = input_text.strip().split('\n\n')

    almanach = {}

    for segment in segments:
        lines = segment.split('\n')
        section_name, values = lines[0].split(':', 1)

        if section_name.strip() == 'seeds':
            almanach[section_name.strip()] = list(map(int, values.strip().split()))
        else:
            map_name = section_name.replace(' map', '').replace('-', '_').strip()
            map_values = [list(map(int, line.replace(',', ' ').split())) for line in lines[1:]]
            almanach[map_name] = map_values

    return almanach


def get_map(source, map_data):
    for map_entry in map_data:
        destination_range_start, source_range_start, range_value = map_entry

        if source_range_start <= source < (source_range_start + range_value):
            return source + (destination_range_start - source_range_start)

    return source

def process_seeds_through_maps(seeds, maps):
    locations = []

    for seed in seeds:
        current_value = seed

        for map_name in ['seed_to_soil', 'soil_to_fertilizer', 'fertilizer_to_water', 
                         'water_to_light', 'light_to_temperature', 
                         'temperature_to_humidity', 'humidity_to_location']:
            current_value = get_map(current_value, maps[map_name])

        locations.append(current_value)

    return locations


with open('input', 'r') as file:
    input_text = file.read()

almanac = parse_almanac(input_text)

locations = process_seeds_through_maps(almanac['seeds'], almanac)
print (min(locations))
