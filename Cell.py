class Cell:
    def __init__(self, color):
        self.color = color
        self.isTaken = False

    def take(self):
        self.isTaken = True
    
