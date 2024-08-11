from Player import *

def printBoard(activePlayer, factory):
    print(activePlayer.name, ':', activePlayer.score)
    activePlayer.board.printBoard()
    factory.printFactory()

def getStartingPlayer(players) -> int:
    for activePlayerIndex, player in enumerate(players, 0):
        if player.toStart:
            player.toStart = False
            return activePlayerIndex
    return 0


def playRound(players, activePlayerIndex, factory) -> Player:
    activePlayer = players[activePlayerIndex]
    while True:
        activePlayer = players[activePlayerIndex]
        playerTurn(activePlayer, factory)
        activePlayerIndex = (activePlayerIndex + 1) % len(players)
        if factory.isEmpty():
            break
    return activePlayer

def playerTurn(activePlayer, factory):
    printBoard(activePlayer, factory)
    try:
        pool = int(input("Select a pool: "))
        color = int(input("Select a color: "))
        row = int(input("Select a row: ")) - 1 #account for the fact that the program list is starts at 0 but player readability should have it start at 1
    except ValueError as e:
        pool = -1
        color = 0
        row = -2
    while not activePlayer.board.isValidMoveBoard(color, row) or not factory.isValidMoveFactory(pool, color):
        print("Move invalid. Try again")
        try:
            pool = int(input("Select a pool: "))
            color = int(input("Select a color: "))
            row = int(input("Select a row: ")) - 1
        except ValueError as e:
            pool = -1
            color = 0
            row = -2

    if pool == 0 and factory.pools[0].hasNegativeTile:
        activePlayer.board.floorLine.addTiles(1)
        factory.pools[0].hasNegativeTile = False
        activePlayer.toStart = True
    chosenTiles = list(filter(lambda tile: tile==color, factory.getPools()[pool].getTiles()))
    if not pool == 0:
        factory.movePoolToCenter(pool, color)
    else:
        factory.pools[0].tiles = list(filter(lambda tile: tile!=color, factory.pools[0].tiles))
    if row == -1:
        activePlayer.board.floorLine.addTiles(len(chosenTiles))
    else:
        overflow = len(chosenTiles) - activePlayer.board.lines[row].numOpenSpaces()
        activePlayer.board.lines[row].fillLine(color, len(chosenTiles))    
        if 0 < overflow:
            activePlayer.board.floorLine.addTiles(overflow)
            

def checkGameOver(players) -> bool:
    for player in players:
        if player.board.isGameOver():
            return True
    return False

def bonusPoints(players):
    for player in players:
        player.addScore(player.bonusPoints())
        print(player.name + ': ' , player.score)


def main():
    names = input("Enter player names separated by comma:").split(",")
    players = list(map(Player, names))
    factory = Factory(numPools=1, numColors=5, tilesPerColor=15)

    while not checkGameOver(players):
        factory.fillAllPools() #make sure there are enough tiles in bag
        activePlayerIndex = getStartingPlayer(players)
        playRound(players, activePlayerIndex, factory) #stops when factory is empty
        for player in players:
            for row in range(0, len(player.board.getLines())):
                if player.board.getLines()[row].isFull():
                    color = player.board.lines[row].getTileColor()
                    player.board.lines[row].resetRow()
                    player.score += player.board.placeTile(color, row)
            #empty fill line subtract it from score
            for cell in player.board.floorLine.arr:
                if cell.isTaken:
                    player.score += cell.color
            player.board.floorLine.resetRow()
    bonusPoints(players)

if __name__ == '__main__':
    main()