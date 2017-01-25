import json
import os
from math import sqrt


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='cp1251') as json_file:
        return json.load(json_file)


def get_biggest_bar(data):
    biggest_bar_num_seats = 0
    biggest_bar_name = ''
    for item in data:
        num_seats_in_bar = item.get('SeatsCount')
        if biggest_bar_num_seats < num_seats_in_bar:
            biggest_bar_num_seats = num_seats_in_bar
            biggest_bar_name = item.get('Name')
    return biggest_bar_name


def get_smallest_bar(data):
    smallest_bar_num_seats = 0
    smallest_bar_name = ''
    for item in data:
        num_seats_in_bar = item.get('SeatsCount')
        if smallest_bar_num_seats >= num_seats_in_bar:
            smallest_bar_num_seats = num_seats_in_bar
            smallest_bar_name = item.get('Name')
    return smallest_bar_name


def get_closest_bar(data, longitude, latitude):
    closest_bar = 0
    closest_bar_name = ''
    for item in data:
        bar_coords = item.get('geoData').get('coordinates')
        bar_latitude, bar_longitude = [float(item) for item in bar_coords]
        distance_from_user = float(sqrt((bar_longitude - longitude)**2 + (bar_latitude - latitude)**2))
        if closest_bar >= distance_from_user or closest_bar is 0:
            closest_bar = distance_from_user
            closest_bar_name = item.get('Name')
    return closest_bar_name


if __name__ == '__main__':
    data = load_data("./bars.json")
    print("\nThe biggest bar is: {}".format(get_biggest_bar(data)))
    print("\nThe smallest bar is: {}".format(get_smallest_bar(data)))
    user_coords = input('\nEnter your coordinates ("longitude;latitude") using semicolon(";") as a splitter> ')
    if ';' in user_coords:
        user_coords = [float(item.strip().replace(',', '.')) for item in user_coords.split(';')]
    else:
        raise IOError("Invalid coordinates!")
    print("\nThe closest bar is: {}".format(get_closest_bar(data, longitude=user_coords[0], latitude=user_coords[1])))
