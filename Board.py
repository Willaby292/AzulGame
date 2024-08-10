from Cell import *
from Factory import *
from Line import *
from FloorLine import *

class Board:
    def __init__(self, size):
        self.size = size
        self.completeH = 0
        self.completeV = 0
        self.completeC = 0
        self.wall = [[0 for i in range(size)] for j in range(size)]
        self.lines = []
        self.floorLine = FloorLine()
        index = size - 1
        for x in range(0, self.size):
            for y in range(0, self.size):
                index = (index + 1) % size
                self.wall[x][y] = Cell(index + 1)
            index = (index - 1) % size
        for y in range(0, self.size):
            self.lines.append(Line(y + 1))

    def getWall(self):
        return self.wall

    def printBoard(self):
        print('-----------')
        for y in range(0, len(self.wall)):
            print(str(self.lines[y].length)+'|', end='')
            for i in range(0, self.size - self.lines[y].length):
                print(' ' + ' ' + ' ', end='|')
            for i in range(0, self.lines[y].length):
                print(' ' + str(self.lines[y].queue[i]) + ' ', end='|')###
            print('#|', end='')
            for x in range(0, len(self.wall)):
                if self.wall[x][y].isTaken:
                    print('-' + str(self.wall[x][y].color) + '-', end='|')
                else:
                    print(' ' + str(self.wall[x][y].color) + ' ', end='|')
            print('')
        print('Floor Line[', end='')
        for i in range(0, 7):
            if self.floorLine.arr[i].isTaken:
                print('',self.floorLine.arr[i].color,'', end='')
            else:
                print('',0,'',end='')
        print(']')


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

        if self.checkCompleteColor(self.wall[x][y].color): #cache color instead
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

    def isValidMoveBoard(self, color, row):
        if row == -1: #this might cause problems
            return True
        else:
            lastInRow = self.lines[row].queue[len(self.lines[row].queue)-1]
        if not lastInRow == color and not lastInRow == 0: # failed
            return False
        for column in range(0, self.size): #failed
            if self.wall[column][row].color == color and self.wall[column][row].isTaken:
                return False
        return True

    def getLines(self):
        return self.lines

    def placeTile(self, color, row):
        for column in range(0,len(self.wall)):
            if self.wall[column][row].color == color and not self.wall[column][row].isTaken: #shouldnt have to check if it is taken. should be done earlier
                self.wall[column][row].take()
                return self.score(column, row)