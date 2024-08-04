from Tile import *
from TileBag import *

class Pool:
    def __init__(self) -> None:
        self.tiles = []

    def fillPool(self, tileBag):
        for i in range(0, 4):
            self.tiles.append(tileBag.removeRandomTile())

    def clearPool(self):
        self.tiles.clear()

    def getTiles(self) -> list:
        return self.tiles
        
    