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
    with open(args.path_to_data, 'r', encoding='utf-8') as file:
        count =0
        films = []
        for line in file:
            film = []
            line = line.split("\t")
            
            if args.year not in line:
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


if __name__ == '__main__':
    args = parser_creation()
    new_map = folium.Map()
    data = read_data(args)
    
    
    new_map.save('your_map.html')
