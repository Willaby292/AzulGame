from Cell import *
from Factory import *
from Line import *


class Board:
    def __init__(self, size):
        self.size = size
        self.completeH = 0
        self.completeV = 0
        self.completeC = 0
        self.wall = [[0 for i in range(size)] for j in range(size)]
        self.lines = []
        index = size - 1
        for x in range(0, self.size):
            for y in range(0, self.size):
                index = (index + 1) % size
                self.wall[x][y] = Cell(index + 1)
            index = (index - 1) % size
        for y in range(0, self.size): #add one to make more readable
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

    def isValidMove(self, x, y) -> bool: #should be made into exception
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

    def getLines(self):
        return self.lines

    def placeTile(self, color, row, column = None):
        if column is None:
            for column in range(0,len(self.wall)): #check if it is taken
                if self.wall[column][row].color == color and not self.wall[column][row].isTaken: #shouldnt have to check if it is taken. should be done earlier
                    self.wall[column][row].take()
                    return self.score(column, row)
        else:
            if not self.wall[column][row].isTaken: #shouldnt have to check if it is taken. should be done earlier
                self.wall[column][row].take()
                return self.score(column, row)