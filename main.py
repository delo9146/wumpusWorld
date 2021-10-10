from wumpusWorld import wumpusWorld
from problemGenerator import problemGenerator

import random
import numpy as np
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) 
from termcolor import cprint 
from pyfiglet import figlet_format

worlds = wumpusWorld
problem = problemGenerator

cprint(figlet_format('WUMPUS WORLD', font='letters'),
       'white', 'on_blue', attrs=['bold', 'blink'])

print("Hello! And welcome to the wumpus world. We are going to start by setting up our caves.")
print("First, give us the probability in which you'd like to encounter pits and wumpi in the caves.")

# getting caves initialized of random sizes 
caves = worlds.worldGenerator()


pits = input("Probability (0-.9) of generating a pit: ")
whatsLeft = .9 - float(pits)
wumpi = input("Probability (0-" + str(whatsLeft) + ") of generating a wumpi: ")


caves = problem.generateWorld(caves, wumpi, pits)
