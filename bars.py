import json
import sys
import math

if len(sys.argv) == 1:
    sys.exit('Path to file is not found!')

file_path = sys.argv[1]


def load_data(file_path):
    with open(file_path, encoding='utf8') as file_data:
        return json.loads(file_data.read())


def get_biggest_bar(info):
    return max(info, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(info):
    return min(info, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_closest_bar(info, longitude, latitude):
    return min(info, key=lambda x:
        math.sqrt((x['geometry']['coordinates'][0] - longitude)**2 +
                 (x['geometry']['coordinates'][1] - latitude)**2))


def output(got_data):
    print('    Name: {}'
          .format(got_data['properties']['Attributes']['Name']), '\n',
          '   Number of seats: {}'
          .format(got_data['properties']['Attributes']['SeatsCount']), '\n',
          '   Coordinates: {}, {}'
          .format(got_data['geometry']['coordinates'][0],
                  got_data['geometry']['coordinates'][1]))


if __name__ == '__main__':
    try:
        longitude = float(input('Enter your longitude: '))
        latitude = float(input('Enter your latitude: '))
    except ValueError:
        sys.exit('Wrong coordinate!')
    print('The BIGGEST bar is:')
    output(get_biggest_bar(load_data(file_path)['features']))
    print('The SMALLEST bar is:')
    output(get_smallest_bar(load_data(file_path)['features']))
    print('The CLOSEST bar is:')
    output(get_closest_bar(load_data(file_path)['features'], longitude, latitude))