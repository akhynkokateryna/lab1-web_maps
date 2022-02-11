"main.py"

import argparse
import math
import folium
from geopy import Nominatim


def parser_creation():
    """Creates parser"""
    parser = argparse.ArgumentParser(description= "Creates html file with map using parameters")
    parser.add_argument('year', type = str, help = "Defines films of what year will be chosen")
    parser.add_argument('latitude', type = str, help = """Latitude of location around
    which films will be found""")
    parser.add_argument('longitude', type = str, help = """Longtitude of location around
    which films will be found""")
    parser.add_argument('path_to_data', type = str, help = "Path to file with films dataset")
    return parser.parse_args()


def read_data(year, latitude, longitude, path_to_data):
    """Reads data from file and creates list with films of the
    needed year
    """
    with open(path_to_data, 'r', encoding='utf-8') as file:
        count = 0
        films = []
        for line in file:
            film = []
            line = line.split("\t")

            if year not in line:
                continue

            if count >= 14:    #not to include first lines of the file without important info
                paren1_index = line[0].index('"')
                paren2_index = line[0].index('" ')
                film.append(line[0][paren1_index+2:paren2_index])

                bracket1_index = line[0].index('(')
                bracket2_index = line[0].index(')')
                film.append(line[0][bracket1_index+1:bracket2_index])

                if "," not in line[-1]:
                    film.append(line[-2].rstrip("\n"))
                else:
                    film.append(line[-1].rstrip("\n"))

            count += 1

            if len(film) != 0:
                films.append(film)
    return films


def get_coordinates(data, geolocator):
    """Gets coordinates from location of the place"""
    for num, location in enumerate(data):
        coord = geolocator.geocode(location[2], timeout = None)
        if coord is None:
            continue
        data[num].append((coord.latitude, coord.longitude))
    return data


def get_distance(year, latitude, longitude, coords):
    """Gets distances from location of the place"""
    for num, _ in enumerate(coords):
        data[num].append(12734.889 * math.asin(math.sqrt((math.sin
        ((coords[num][3][0]-latitude)/2)) ** 2
        + math.cos(coords[num][3][0]) * math.cos(latitude)
        * (math.sin((longitude-coords[num][3][1])/2)) ** 2)))
    return coords


# def 


if __name__ == '__main__':
    geolocator = Nominatim(user_agent="main.py")
    args = parser_creation()
    year = args.year
    latitude = args.latitude
    longitude = args.longitude
    path_to_data = args.path_to_data

    new_map = folium.Map()
    data = read_data(year, latitude, longitude, path_to_data)
    coords = get_coordinates(data, geolocator)
    distances = get_distance(year, latitude, longitude, coords)
    # distances = sorted(distances, key=lambda x: x[4])
    print(data)
    
    # new_map.save('your_map.html')
