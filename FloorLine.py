from Cell import *

class FloorLine:
    def __init__(self, length: int=7):
        cellValues = [-1, -1, -2, -2, -2, -3, -3]
        self.length = length
        self.arr = []
        self.index = 0
        for i in range(0, length):
            self.arr.append(Cell(cellValues[i]))

    def isFull(self) -> bool:
        if self.arr[self.length-1].isTaken:
            return True
        return False

    def resetRow(self) -> int:
        self.arr.clear()
        for i in range(0, self.length):
            self.queue.append(0)

    def addTiles(self, numTiles):
        for i in range(0, numTiles):
            if not self.isFull():
                self.arr[self.index].isTaken = True
                self.index +=1