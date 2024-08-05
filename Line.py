def checkEnoughSpaceInRow(row, numTiles):
    numOpenSpaces = len(list(filter(lambda tile: tile == 0 ,row)))
    if numOpenSpaces < numTiles:
        raise Exception("Not enough space in selected row")

class Line:
    def __init__(self, length: int):
        self.length = length
        self.queue = []
        for i in range(0, length):
            self.queue.append(0)

    def fillLine(self, color: int, numTiles: int):
        for i in range(0, numTiles):
            self.queue.pop(0)
            self.queue.append(color)

    def isFull(self) -> bool:
        if 0 in self.queue:
            return False
        return True

    def resetRow(self) -> int:
        self.queue.clear()
        for i in range(0, self.length):
            self.queue.append(0)

    def getTileColor(self) -> int:
        return self.queue[len(self.queue)-1]
