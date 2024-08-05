import math
import random

class TileBag:
    def __init__(self, numColors: int=5, tilesPerColor: int=15) -> None:
        self.allTiles = {}
        self.numColors = numColors
        self.tilesPerColor = tilesPerColor
        for i in range(1, numColors+1):
            self.allTiles[i] = tilesPerColor


    def removeRandomTile(self) -> int:
        colorsWithTiles = []
        for i in self.allTiles:
            if self.allTiles[i] > 0:
                colorsWithTiles.append(i)
        chosenColor = random.randint(0, len(colorsWithTiles)-1)
        self.allTiles[colorsWithTiles[chosenColor]] -= 1
        return colorsWithTiles[chosenColor]

    def refillBag(self):
        for i in range(0, self.numColors):
            self.allTiles[i] = self.tilesPerColor