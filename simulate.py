import pybullet as p
import time as t

physicsClient = p.connect(p.GUI)

for i in range(1000):
    p.stepSimulation()
    print(i)
    t.sleep(1/60)

p.disconnect()