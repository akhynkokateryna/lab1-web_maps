"main.py"

import argparse
import folium


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


def read_data(args):
    """Reads data from file and creates list with films of the
    needed year"""
    films = []
    with open(args.path_to_data, 'r', encoding='utf-8') as file:
        for line in file:
            film = []
            film.append()


def create_map(args):
    new_map = folium.Map()
    data = read_data(args)
    

    map.save('your_map.html')


if __name__ == '__main__':
    args = parser_creation()
    create_map(args)
