from os import stat
import numpy as np
import random

''' Contributors: Derek Logan
----------------------------------------------------------------------------------------------
problemGenerator takes a list of caves in the generateWorld method as well as the probabilities
which have been read in through user input in the main class. It then distributes this information
to the setGold, setWumpi, and setPits methods to generate the caves so they are ready for exploration.
----------------------------------------------------------------------------------------------
'''

class problemGenerator:
    

    # --------------------------------------------------------------------------------------------
    # The setGold method selects one of the empty cells at random using a randint which meets the requirement of 
    # setting the gold using a uniform probability distribution. randint returns random integers from the discrete uniform 
    # distribution.

    @staticmethod
    def setGold(array):
        #getting dimensions of current cave to know limits of where to set gold
        caveDim = np.shape(array)
        row = random.randint(0,caveDim[0]-1)
        col = random.randint(0,caveDim[1]-1)
        #setting a cell in the array to G to indicate gold location
        array[row, col] = 'G'

        return array

    # --------------------------------------------------------------------------------------------
    # The setWumpi method first picks a random number of cells to populate with the notorius Wumpus. 
    # No more than a quarter of the board will be filled with wumpi. Once number is picked, board
    # is populated by assigning cells using a uniform probability distribution.

    @staticmethod
    def setWumpi(array, num):
        count = 0
        caveDim = np.shape(array)
        dim = caveDim[0] * caveDim[1]
        numWumpi = round(dim * float(num))

        print("This cave will have a total of " + str(numWumpi) + " Wumpi... Good luck!")
        
        while count != numWumpi:
            row = random.randint(0,caveDim[0]-1)
            col = random.randint(0,caveDim[1]-1)
            if array[row, col] == '':
                array[row,col] = 'W'
                count += 1
            else: 
                continue

        return(array)

    # --------------------------------------------------------------------------------------------
    # The setPits method first picks a random number of cells to populate with deadly, spike filled pits. 
    # No more than a quarter of the board will be filled with pits. Once number is picked, board
    # is populated by assigning cells using a uniform probability distribution.

    @staticmethod
    def setPits(array, num):
        count = 0
        caveDim = np.shape(array)
        dim = caveDim[0] * caveDim[1]

        numPits = round(dim * float(num))

        print("This cave will have a total of " + str(numPits) + " Pits... Good luck!")
        
        while count != numPits:
            row = random.randint(0,caveDim[0]-1)
            col = random.randint(0,caveDim[1]-1)
            if array[row, col] == '':
                array[row,col] = 'P'
                count += 1
            else: 
                continue

        return(array)

    # --------------------------------------------------------------------------------------------
    # The generateWorld method distributes the caves so that they can be generated with obstacles

    @staticmethod
    def generateWorld(caves, wumpi, pits):
        problem = problemGenerator

        # setting the gold for all caves
        for i in range(len(caves)):
            caves[i] = problem.setGold(caves[i])
        
        # setting random number of wumpi in the cave
        for i in range(len(caves)):
            caves[i] = problem.setWumpi(caves[i], wumpi)

        # setting random number of pits in the cave
        for i in range(len(caves)):
            caves[i] = problem.setPits(caves[i], pits)
            print(caves[i])

        return caves

        