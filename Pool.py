from Tile import *
from TileBag import *

class Pool:
    def __init__(self) -> None:
        self.tiles = []

    def fillPool(self, tileBag):
        for i in range(0, 4):
            self.tiles.append(tileBag.removeRandomTile())

    def clearPool(self) -> None:
        self.tiles.clear()

    def getTiles(self) -> list:
        return self.tiles

    def removeTile(self, color) -> None:
        numColor = 0
        for tile in self.tiles:
            if tile == color:
                numColor += 1
        for i in range(0, numColor):
            self.tiles.remove(color)