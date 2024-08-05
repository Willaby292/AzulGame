from Pool import *

def checkEnoughTilesToFillPools(numPools, numColors, tilesPerColor): #needs to be implemented
    totalTiles = numColors * tilesPerColor
    if totalTiles/numPools < 4:
        raise Exception("Cannot start game. Not enough tiles["+ str(totalTiles) +"] to fill pools["+str(numPools)+"]")

class Factory:
    def __init__(self, numPools: int=5, numColors: int=5, tilesPerColor:int = 15):
        self.numPools = numPools
        self.pools = {}
        try:
            checkEnoughTilesToFillPools(numPools, numColors, tilesPerColor)
            self.tileBag = TileBag(numColors, tilesPerColor) #need to check that the facroty has enough tiles to fill the pools
        except Exception as e:
            print(e)
            print('Defaulting tile count')
            self.numPools = 5
            self.tileBag = TileBag()
        for i in range(0, self.numPools + 1): #add one to account for center pool
            self.pools[i] = Pool()

    def fillAllPools(self) -> None:
        for pool in range(1, len(self.pools)):
            self.pools[pool].fillPool(self.tileBag)

    def getPools(self):
        return self.pools

    def printFactory(self):
        for pool in self.pools:
            print(str(pool)+':', end='')
            print(self.pools[pool].getTiles(), end='  ')
        print('')
        print('-----------')

    def movePoolToCenter(self, pool, color):
        self.pools[pool].removeTile(color)
        for i in self.pools[pool].getTiles():
            self.pools[0].tiles.append(i)

        self.pools[pool].clearPool()

    def isEmpty(self):
        for poolNum in self.pools:
            if not self.pools[poolNum].isEmpty():
                return False
        return True