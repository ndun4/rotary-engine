"""Makes the maps"""

import itertools
import noise

#globals
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3


class MapTile:
    """Our map will need to be divided up into individual tiles. The tiles
    will help determine what can be seen from a player's location, as well
    as what the player can interact with in that location."""

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.coords = (self.x, self.y)
        self.elevation = None #for future use, maybe

        #links to other tiles go here TODO

        self.terrain = [] #TODO
        self.contains = None #TODO
        self.view_from = {}


class Seed(MapTile):

    def __init__(self, x, y):
        super().__init__(x, y)


def generate_map(x_len, y_len):

    points = list(itertools.product(range(x_len), (range(y_len))))

    #noisemap = map(noise.snoise2)
    all_tiles = []
    for i in points:

        new_tile = MapTile(*i)
        all_tiles.append(new_tile)
        
    print('{} new game tiles created'.format(len(all_tiles)))
    



