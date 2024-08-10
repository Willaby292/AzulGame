from TileBag import *

class Pool:
    def __init__(self) -> None:
        self.hasNegativeTile = False
        self.tiles = []

    def fillPool(self, tileBag):
        for i in range(0, 4):
            self.tiles.append(tileBag.removeRandomTile())

    def clearPool(self) -> None:
        self.tiles.clear()

    def getTiles(self) -> list:
        return self.tiles

    def removeTile(self, color) -> None:
        self.tiles = list(filter(lambda tile: tile != color, self.tiles))

    def isEmpty(self):
        if not self.tiles:
            return True
        return False

    def sortPool(self) -> None:
        self.tiles.sort()