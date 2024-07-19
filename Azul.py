from Player import *

def playRound(players, activePlayerIndex) -> Player:
    activePlayer = players[activePlayerIndex]
    starter = activePlayer.name
    while True:
        activePlayerIndex = (activePlayerIndex + 1) % len(players)
        activePlayer = players[activePlayerIndex]
        playerTurn(activePlayer)
        print(activePlayer.score)
        if starter == activePlayer.name:
            break
    return activePlayer


def playerTurn(activePlayer):
    print(activePlayer.name, ': ')
    activePlayer.board.printBoard()
    coordinates = input("Select a coordinate: ").split(",")
    x = int(coordinates[0])
    y = int(coordinates[1])
    while not activePlayer.board.isValidMove(x,abs(y - (activePlayer.board.size - 1))):
        coordinates = input("Select a coordinate: ").split(",")
        x = int(coordinates[0])
        y = int(coordinates[1])
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

    activePlayerIndex = -1

    while not checkGameOver(players):
        playRound(players, activePlayerIndex)
    
    bonusPoints(players)

if __name__ == '__main__':
    main()