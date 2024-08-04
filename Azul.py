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
    pool = int(input("Select a pool: "))
    print(factory.getPools()[pool].getTiles()) #print list of options
    color = int(input("Select a color: "))
    while not color in factory.getPools()[pool].getTiles():
        pool = int(input("Select a pool: "))
        print(factory.getPools()[pool].getTiles()) #print list of options
        color = int(input("Select a color: "))
    activePlayer.board.wall[x][abs(y - (activePlayer.board.size - 1))].take()
    activePlayer.addScore(activePlayer.board.score(x,y))

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