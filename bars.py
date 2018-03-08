import json
import sys
import math


def load_data(file_path):
    with open(file_path, encoding='utf8') as file_data:
        return json.loads(file_data.read())


def get_biggest_bar(bars):
    return max(bars,
               key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bars):
    return min(bars,
               key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_closest_bar(bars, longitude, latitude):
    return min(bars,
               key=lambda x: math.sqrt((x['geometry']['coordinates'][0] -
               longitude)**2 + (x['geometry']['coordinates'][1] - latitude)**2))


def give_output(data_about_bars):
    print('    Name: {}'
          .format(data_about_bars['properties'] ['Attributes']['Name']),
          '\n',
          '   Number of seats: {}'
          .format(data_about_bars['properties']['Attributes']['SeatsCount']),
          '\n',
          '   Coordinates: {}, {}'
          .format(data_about_bars['geometry']['coordinates'][0],
                  data_about_bars['geometry']['coordinates'][1]))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit('Path to file is not found!')
    file_path = sys.argv[1]
    try:
        longitude = float(input('Enter your longitude: '))
        latitude = float(input('Enter your latitude: '))
    except ValueError:
        sys.exit('Wrong coordinate!')
    strings_from_json = load_data(file_path)['features']
    print('The BIGGEST bar is:')
    give_output(
        get_biggest_bar(
            strings_from_json))
    print('The SMALLEST bar is:')
    give_output(
        get_smallest_bar(
            strings_from_json))
    print('The CLOSEST bar is:')
    give_output(
        get_closest_bar(
            strings_from_json, longitude, latitude))