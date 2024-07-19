from Cell import *

class Board:
    def __init__(self, size):
        self.size = size
        self.completeH = 0
        self.completeV = 0
        self.completeC = 0
        self.wall = [[0 for i in range(size)] for j in range(size)]
        index = size - 1
        for x in range(0, self.size):
            for y in range(0, self.size):
                index = (index + 1) % size
                self.wall[x][y] = Cell(str(index))
            index = (index - 1) % size

    def getWall(self):
        return self.wall
    
    def printBoard(self):
        print('-----------')
        for y in range(0, len(self.wall)):
            print('|', end='')
            for x in range(0, len(self.wall)):
                if self.wall[x][y].isTaken:
                    print('-' + self.wall[x][y].color + '-', end='|')
                else:
                    print(' ' + self.wall[x][y].color + ' ', end='|')
            print('')        
        print('-----------')


    def recur(self, dx, dy, x, y) -> int:
        x += dx
        y += dy
        if not 0 <= x < self.size or not 0 <= y < self.size:
            return 0
        elif not self.wall[x][y].isTaken:
            return 0
        return 1 + self.recur(dx, dy, x, y)


    def checkCompleteColor(self, color):
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.wall[x][y].color == color:
                    if not self.wall[x][y].isTaken:
                        return False
        return True


    def score(self, x, y) -> int:
        score = 1
        hScore = 0
        vScore = 0

        vScore += self.recur(0, 1, x, y)
        vScore += self.recur(0, -1, x, y)
        hScore += self.recur(1, 0, x, y)
        hScore += self.recur(-1, 0, x, y)

        if vScore and hScore:
            score += 1
        if vScore == self.size - 1:
            self.completeV += 1
        if hScore == self.size - 1:
            self.completeH += 1

        if self.checkCompleteColor(self.wall[x][y].color):
            self.completeC += 1

        score = vScore + hScore + score
        return score
    
    def isGameOver(self) -> bool:
        for y in range(0, self.size):
            index = 0
            for x in range(0, self.size):
                if not self.wall[x][y].isTaken:
                    break
                index += 1
                if index == self.size:
                    return True
        return False
    
    def isValidMove(self, x, y) -> bool:
        if not self.size > x >= 0:
            print('--Invalid Move--')
            return False
        if not self.size > y >= 0:
            print('--Invalid Move--')
            return False
        if self.wall[x][y].isTaken:
            print('--Invalid Move--')
            return False
        return True