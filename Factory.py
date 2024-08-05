from Pool import *

#Structure of factory should be map of pools -> array of tiles
# ie map   1 : (blue, blue, black, white), 2 : (white, white, yellow, red) 3: ()
# they will either have 4 tiles, or zero tiles except for the center pool which will hold 0-unlimited tiles and will initialize with a -1 tile
# the -1 tile will be represented by a boolean hasMinusTile which is set to True until a player picks from the center pool

class Factory:
    def __init__(self, numPools: int=5):
        self.numPools = numPools
        self.pools = {}
        self.tileBag = TileBag()
        for i in range(0, numPools + 1): #add one to account for center pool
            self.pools[i] = Pool()

    def fillAllPools(self) -> None:
        for pool in self.pools:
            self.pools[pool].fillPool(self.tileBag)
        self.pools[0].clearPool()

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
