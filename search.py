import os
from time import sleep

for i in range(5):
    os.system('python generate.py')
    sleep(1)
    os.system('python simulation.py')