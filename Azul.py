from Player import *

def playRound(players, activePlayerIndex, factory) -> Player:
    activePlayer = players[activePlayerIndex]
    starter = activePlayer.name
    while True:
        activePlayerIndex = (activePlayerIndex + 1) % len(players)
        activePlayer = players[activePlayerIndex]
        playerTurn(activePlayer, factory)
        print(activePlayer.score)
        if starter == activePlayer.name:
            break
    return activePlayer

def playerTurn(activePlayer, factory):
    print(activePlayer.name, ': ')
    activePlayer.board.printBoard()
    factory.printFactory()
    pool = int(input("Select a pool: "))
    print(factory.getPools()[pool].getTiles()) #print list of options
    color = int(input("Select a color: "))
    row = int(input("Select a row: ")) - 1 #account for the fact that the program list is starts at 0 but player readability should have it start at 1
    while not color in factory.getPools()[pool].getTiles():
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
        print(player.name + ': ' + str(player.score))


def main():
    names = input("Enter player names separated by comma:").split(",")
    players = list(map(Player, names))
    factory = Factory()
    factory.fillAllPools()

    activePlayerIndex = -1

    while not checkGameOver(players):
        playRound(players, activePlayerIndex, factory)

    bonusPoints(players)

if __name__ == '__main__':
    main()