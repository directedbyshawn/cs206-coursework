import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.values = np.zeros(c.ITERATIONS)
        self.Prepare_To_Act()
        print(self.jointName)

    def Prepare_To_Act(self):
        self.amplitude = np.pi/8
        if self.jointName == b'Torso_BackLeg':
            self.frequency = 5
        else:
            self.frequency = 10
        self.offset = 0
        self.motorValues = [self.amplitude * np.sin(self.frequency * x + self.offset) for x in np.linspace(0, 2*np.pi, c.ITERATIONS)]

    def Set_Value(self, robotId, step):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[step],
            maxForce = c.max_force
        )

    def Save_Values(self):
        np.save(f'data/motor_{self.jointName}_values.npy', self.values)