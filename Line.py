class Line:
    def __init__(self, row: int, length: int):
        self.length = length
        self.row = row
        self.queue = []
        for i in range(0, length):
            self.queue.append(0)
        print('hello')


    def fillLine(self, color: int, numTiles: int) -> bool: #should make sure that its not adding to many. not sure where that needs to be
        numZeros = 0
        for i in self.queue:
            if i == 0:
                numZeros += 1
        if numZeros < numTiles:
            print('not enough space for tiles in this row')
            return False
        for i in range(0, numTiles):
            self.queue.pop(0)
            self.queue.append(color)
        return True