import random

class TileBag:
    def __init__(self, numColors: int=5, tilesPerColor: int=15) -> None: #there is an edge case where youy can make a game with not enough tiles to fill the factory
        self.allTiles = {}
        self.numColors = numColors
        self.tilesPerColor = tilesPerColor
        for i in range(1, numColors + 1):
            self.allTiles[i] = tilesPerColor

    def removeRandomTile(self) -> int:
        availableColors = list(filter(lambda color: self.allTiles[color] >= 1, self.allTiles))
        if not availableColors:
            self.refillBag()
            availableColors = list(filter(lambda color: self.allTiles[color] >= 1, self.allTiles))  #doing it this way means the math is off. Since some tiles will already be on the board
        chosenColor = random.choice(availableColors)
        self.allTiles[chosenColor] -= 1
        return chosenColor

    def refillBag(self):
        for i in range(1, self.numColors + 1):
            self.allTiles[i] = self.tilesPerColor