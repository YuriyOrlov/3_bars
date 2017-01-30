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


def user_enters_coordinates():
    user_coords = input('\nEnter your coordinates ("longitude;latitude") using semicolon(";") as a splitter> ')
    if ';' in user_coords:
        user_coords = [float(item.strip().replace(',', '.')) for item in user_coords.split(';')]
    else:
        raise IOError("Invalid coordinates!")
    return("\nThe closest bar is: {}".format(get_closest_bar(bars_from_file,
                                                             longitude=user_coords[0],
                                                             latitude=user_coords[1])))


def distance_from_user(user_lat, user_lon, dot_coords):
    return float(sqrt((dot_coords[1] - user_lon)**2 + (dot_coords[0] - user_lat)**2))


def get_closest_bar(data, longitude, latitude):
    return min(data, key=lambda x: distance_from_user(user_lon=longitude,
                                                      user_lat=latitude,
                                                      dot_coords=x.get('geoData').get('coordinates')))['Name']


if __name__ == '__main__':
    bars_from_file = load_data("./bars.json")
    print("\nThe biggest bar is: {}".format(get_biggest_bar(bars_from_file)))
    print("\nThe smallest bar is: {}".format(get_smallest_bar(bars_from_file)))
    print(user_enters_coordinates())
