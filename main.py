"main.py"

import argparse
import math
import folium
from geopy import Nominatim


def parser_creation():
    """Creates parser"""
    parser = argparse.ArgumentParser(description= "Creates html file with map using parameters")
    parser.add_argument('year', type = str, help = "Defines films of what year will be chosen")
    parser.add_argument('latitude', type = float, help = """Latitude of location around
    which films will be found""")
    parser.add_argument('longitude', type = float, help = """Longtitude of location around
    which films will be found""")
    parser.add_argument('path_to_data', type = str, help = "Path to file with films dataset")
    return parser.parse_args()


def read_data(year, path_to_data):
    """Reads data from file and creates list with films of the
    needed year
    """
    with open(path_to_data, 'r', encoding='utf-8', errors="ignore") as file:
        count = 0
        films = []
        for line in file:
            film = []
            line = line.split("\t")

            if count >= 14:    #not to include first lines of the file without important info
                try:
                    bracket1_index = line[0].index('(')
                    if '"' in line[0]:
                        paren1_index = line[0].index('"')
                        paren2_index = line[0].index('" ')
                        film.append(line[0][paren1_index+1:paren2_index])
                    else:
                        film.append(line[0][:bracket1_index-1])

                    bracket2_index = line[0].index(')')
                    film.append(line[0][bracket1_index+1:bracket2_index])

                    if "," not in line[-1]:
                        film.append(line[-2].rstrip("\n"))
                    else:
                        film.append(line[-1].rstrip("\n"))
                except ValueError:
                    continue

            count += 1

            # if year not in line:
            #     continue

            if len(film) != 0:
                films.append(film)
    print(films)
    return films


def get_coordinates(data, geolocator):
    """Gets coordinates from location of the place"""
    for num, location in enumerate(data):
        coord = geolocator.geocode(location[2], timeout = None)
        if coord is None:
            continue
        data[num].append((coord.latitude, coord.longitude))
    return data


def get_distance(latitude, longitude, coords):
    """Gets distances from location of the place"""
    for num, _ in enumerate(coords):
        coords[num].append(12734.889 * math.asin(math.sqrt((math.sin
        ((coords[num][3][0]-latitude)/2)) ** 2
        + math.cos(coords[num][3][0]) * math.cos(latitude)
        * (math.sin((longitude-coords[num][3][1])/2)) ** 2)))
    return coords


def marker_layers(distances1):
    "Creates a new layer on a map with markers of locations"
    layer = folium.FeatureGroup(name="closest locations")
    for num, loc in enumerate(distances1):
        new_map.add_child(layer.add_child(folium.Marker(location=[loc[num][3][0],\
        loc[num][3][1]], popup=loc[num][0])))

    my_layer = folium.FeatureGroup(name="Lviv location")
    new_map.add_child(my_layer.add_child(folium.Marker(location=[49.8397, 24.0297], popup='Lviv')))


if __name__ == '__main__':
    geolocator1 = Nominatim(user_agent="main.py")
    args = parser_creation()
    year1 = args.year
    latitude1 = args.latitude
    longitude1 = args.longitude
    path_to_data1 = args.path_to_data

    new_map = folium.Map()
    data1 = read_data(year1, path_to_data1)

    coords1 = get_coordinates(data1, geolocator1)
    distances = get_distance(latitude1, longitude1, coords1)
    distances = sorted(distances, key=lambda x: x[4])[:9]
    marker_layers(distances)

    new_map.add_child(folium.LayerControl())
    new_map.save('your_map.html')
