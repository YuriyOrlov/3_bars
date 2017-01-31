import json
import os
from math import sqrt


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='cp1251') as json_file:
        return json.load(json_file)


def get_biggest_bar(data):
    return max(data, key=lambda x: x['SeatsCount'])['Name']


def get_smallest_bar(data):
    return min(data, key=lambda x: x['SeatsCount'])['Name']


def receiving_user_coordinates():
    user_coords = input('\nEnter your coordinates ("longitude;latitude") using semicolon(";") as a splitter> ')
    if ';' in user_coords:
        return [float(item.strip().replace(',', '.')) for item in user_coords.split(';')]
    else:
        raise ValueError("Invalid coordinates!")


def show_closest_bar(lat_lng_list):
    return "\nThe closest bar is: {}".format(calculate_closest_bar(bars_from_file,
                                                                   longitude=lat_lng_list[0],
                                                                   latitude=lat_lng_list[1]))


def distance_from_user(user_lat, user_lon, dot_coords):
    return float(sqrt((dot_coords[1] - user_lon)**2 + (dot_coords[0] - user_lat)**2))


def calculate_closest_bar(data, longitude, latitude):
    return min(data, key=lambda x: distance_from_user(user_lon=longitude,
                                                      user_lat=latitude,
                                                      dot_coords=x['geoData']['coordinates']))['Name']


if __name__ == '__main__':
    bars_from_file = load_data("./bars.json")
    print("\nThe biggest bar is: {}".format(get_biggest_bar(bars_from_file)))
    print("\nThe smallest bar is: {}".format(get_smallest_bar(bars_from_file)))
    print(show_closest_bar(receiving_user_coordinates()))
