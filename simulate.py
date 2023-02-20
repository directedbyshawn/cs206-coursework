from simulation import SIMULATION

import pybullet as p
import numpy as np
import constants as c

simulation = SIMULATION()

simulation.Run()

targetAnglesBL = [c.amplitudeBL * np.sin(c.frequencyBL * x + c.phaseOffsetBL) for x in np.linspace(0, 2*np.pi, c.ITERATIONS)]
targetAnglesFL = [c.amplitudeFL * np.sin(c.frequencyFL * x + c.phaseOffsetFL) for x in np.linspace(0, 2*np.pi, c.ITERATIONS)]
#np.save('data/sin_values.npy', targetAngles)



np.save('data/bl_sensor_values.npy', backlegSensorValues)
np.save('data/fl_sensor_values.npy', frontlegSensorValues)

p.disconnect()