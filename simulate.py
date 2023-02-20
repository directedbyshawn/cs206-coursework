from simulation import SIMULATION

import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c

simulation = SIMULATION()



backlegSensorValues = np.zeros(c.ITERATIONS)
frontlegSensorValues = np.zeros(c.ITERATIONS)

targetAnglesBL = [c.amplitudeBL * np.sin(c.frequencyBL * x + c.phaseOffsetBL) for x in np.linspace(0, 2*np.pi, c.ITERATIONS)]
targetAnglesFL = [c.amplitudeFL * np.sin(c.frequencyFL * x + c.phaseOffsetFL) for x in np.linspace(0, 2*np.pi, c.ITERATIONS)]
#np.save('data/sin_values.npy', targetAngles)

for i in range(c.ITERATIONS):
    p.stepSimulation()
    backlegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link('BackLeg')
    frontlegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link('FrontLeg')
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = simulation.robot.robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAnglesBL[i],
        maxForce = c.max_force
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = simulation.robot.robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAnglesFL[i],
        maxForce = c.max_force
    )
    t.sleep(c.sleep)

np.save('data/bl_sensor_values.npy', backlegSensorValues)
np.save('data/fl_sensor_values.npy', frontlegSensorValues)

p.disconnect()