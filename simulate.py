import pybullet as p
import time as t
import pybullet_data

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

# set gravity, create floor plane, load link
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

for i in range(1000):
    p.stepSimulation()
    print(i)
    t.sleep(1/60)

p.disconnect()