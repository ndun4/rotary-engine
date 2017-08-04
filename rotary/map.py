"""Makes the maps"""

class MapTile(object):
    """Our map will need to be divided up into individual tiles. The tiles
    will help determine what can be seen from a player's location, as well
    as what the player can interact with in that location."""

    def __init__(self, pos_x, pos_y, **kwargs):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.elevation = None #for future use, maybe

        #links to other tiles go here TODO

        self.terrain = [] #TODO
        self.contains = None #TODO



