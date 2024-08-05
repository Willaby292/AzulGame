from Player import *

#TODO fix players being able to add to rows that are taken by different colors
#TODO add negitive points for picking center first
#TODO add negitive row for overflow tiles
#TODO fix turn order so each round starts with player who took the center first in last round

def printBoard(activePlayer, factory):
    print(activePlayer.name, ':', activePlayer.score)

    activePlayer.board.printBoard()
    factory.printFactory()

def playRound(players, activePlayerIndex, factory) -> Player:
    activePlayer = players[activePlayerIndex]
    while True:
        activePlayerIndex = (activePlayerIndex + 1) % len(players)
        activePlayer = players[activePlayerIndex]
        playerTurn(activePlayer, factory)
        if factory.isEmpty():
            break
    return activePlayer

def playerTurn(activePlayer, factory):
    printBoard(activePlayer, factory)
    pool = int(input("Select a pool: "))
    print(factory.getPools()[pool].getTiles()) #print list of options
    color = int(input("Select a color: "))
    row = int(input("Select a row: ")) - 1 #account for the fact that the program list is starts at 0 but player readability should have it start at 1
    while not color in factory.getPools()[pool].getTiles():# can use the check fill line in Line.py
        print("pool color combo doesnt exist")
        pool = int(input("Select a pool: "))
        print(factory.getPools()[pool].getTiles()) #print list of options
        color = int(input("Select a color: "))
        row = int(input("Select a row: ")) - 1

    chosenTiles = []
    for tile in factory.getPools()[pool].getTiles(): #should be a func?
        if tile == color:
            chosenTiles.append(tile)
    activePlayer.board.lines[row].fillLine(color, len(chosenTiles))
    if not pool == 0:
        factory.movePoolToCenter(pool, color)
    else:
        factory.pools[0].tiles = list(filter((color).__ne__, factory.pools[0].tiles))

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
    activePlayerIndex = -1

    while not checkGameOver(players):
        factory.fillAllPools() #make sure there are enough tiles in bag
        playRound(players, activePlayerIndex, factory) #stops when factory is empty
        for player in players:
            for row in range(0, len(player.board.getLines())):
                if player.board.getLines()[row].isFull():
                    color = player.board.lines[row].getTileColor()
                    player.board.lines[row].resetRow()
                    player.score += player.board.placeTile(color, row)

    bonusPoints(players)

if __name__ == '__main__':
    main()