import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

# set gravity, create floor plane, load link
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backlegSensorValues = np.zeros(1000)

for i in range(1000):
    p.stepSimulation()
    backlegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    t.sleep(1/60)

np.save('data/bl_sensor_values.npy', backlegSensorValues)

p.disconnect()