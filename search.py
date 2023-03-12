import os
from time import sleep
from hillclimber import HILL_CLIMBER
from solution import SOLUTION

hc = HILL_CLIMBER()
hc.Evolve()

# for i in range(5):
#     os.system('python generate.py')
#     sleep(1)
#     os.system('python simulation.py')