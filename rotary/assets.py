"""We need to define the models for all the data being passed around between
characters, map tiles, etc. Since most of them need similar APIs, we will use
some base classes."""

class Container(object):

    def __init__(self):

        self._assets = []

    @property
    def assets(self):
        return self._assets

    def add(self, asset, verbose=False):
        self._assets.append(asset)
        if verbose == True:
            return self._assets


class Item(object):

    def __init__(self, name):

        self.name = name

    def __repr__(self):
        return '{}'.format(name)
