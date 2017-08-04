"""Makes the maps"""

import itertools

#globals
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3


class MapTile(object):
    """Our map will need to be divided up into individual tiles. The tiles
    will help determine what can be seen from a player's location, as well
    as what the player can interact with in that location."""

    def __init__(self, pos_x, pos_y, **kwargs):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.coords = (self.pos_x, self.pos_y)
        self.elevation = None #for future use, maybe

        #links to other tiles go here TODO

        self.terrain = [] #TODO
        self.contains = None #TODO
        self.view_from = {}


def generate_map(x_len, y_len):

    points = list(itertools.product(range(x_len), (range(y_len))))
    all_tiles = []
    for i in points:

        new_tile = MapTile(*i)
        all_tiles.append(new_tile)
        
    print('{} new game tiles created'.format(len(all_tiles)))
    



