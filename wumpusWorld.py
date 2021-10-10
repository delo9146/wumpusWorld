import numpy as np 
import random

class wumpusWorld:
    
    @staticmethod
    def worldGenerator():
        caveList = []
        for i in range(1,11):
            current = np.full((random.randrange(5,25,5), random.randrange(5,25,5)), "")
            caveList.append(current)

        return caveList