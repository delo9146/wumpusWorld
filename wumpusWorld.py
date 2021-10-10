import numpy as np 
import random

''' Contributors: Derek Logan
----------------------------------------------------------------------------------------------
wumpusWorld has one function. This is called to create exactly 10 cave systems/wumpus worlds.
Each cave will be a square and sized as 5x5 to 25x25 in steps of 5
----------------------------------------------------------------------------------------------
'''

class wumpusWorld:
    

    # --------------------------------------------------------------------------------------------
    # The worldGenerator method creates a list of caves and generates sizes randomly

    @staticmethod
    def worldGenerator():
        caveList = []
        for i in range(1,11):
            current = np.full((random.randrange(5,25,5), random.randrange(5,25,5)), "")
            caveList.append(current)

        return caveList