from Board import *

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.board = Board(5)

    def addScore(self, score):
        self.score += score

    def bonusPoints(self):
        hTotal = self.board.completeH * 2
        vTotal = self.board.completeV * 7
        cTotal = self.board.completeC * 10
        
        totalBonus = hTotal + vTotal + cTotal
        return totalBonus
