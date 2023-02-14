import numpy as np
import matplotlib.pyplot as plt

backlegSensorValues = np.load('data/bl_sensor_values.npy')
frontlegSensorValues = np.load('data/fl_sensor_values.npy')
sinValues = np.load('data/sin_values.npy')

plt.plot(sinValues)
plt.show()

'''
plt.plot(backlegSensorValues, label='Back Leg', linewidth=3)
plt.plot(frontlegSensorValues, label='Front Leg')
plt.legend()
plt.show()
'''