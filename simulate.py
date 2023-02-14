import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

ITERATIONS = 1000

# Motor control settings for back leg
amplitudeBL = np.pi/8
frequencyBL = 10
phaseOffsetBL = 0

# Motor control settings for front leg
amplitudeFL = np.pi/8
frequencyFL = 10
phaseOffsetFL = np.pi/4

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

# set gravity, create floor plane, load link
p.setGravity(0,0,-9.8)
planeId = p.loadURDF('plane.urdf')
robotId = p.loadURDF('body.urdf')
p.loadSDF('world.sdf')

pyrosim.Prepare_To_Simulate(robotId)

backlegSensorValues = np.zeros(ITERATIONS)
frontlegSensorValues = np.zeros(ITERATIONS)

targetAnglesBL = [amplitudeBL * np.sin(frequencyBL * x + phaseOffsetBL) for x in np.linspace(0, 2*np.pi, ITERATIONS)]
targetAnglesFL = [amplitudeFL * np.sin(frequencyFL * x + phaseOffsetFL) for x in np.linspace(0, 2*np.pi, ITERATIONS)]
#np.save('data/sin_values.npy', targetAngles)

for i in range(ITERATIONS):
    p.stepSimulation()
    backlegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link('BackLeg')
    frontlegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link('FrontLeg')
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAnglesBL[i],
        maxForce = 500
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAnglesFL[i],
        maxForce = 500
    )
    t.sleep(1/60)

np.save('data/bl_sensor_values.npy', backlegSensorValues)
np.save('data/fl_sensor_values.npy', frontlegSensorValues)

p.disconnect()